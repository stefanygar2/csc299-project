import json
import os
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from typing import List, Dict, Any, Optional

# --- Fixtures for Mocking ---

@pytest.fixture
def mock_path(tmp_path):
    """
    Creates a temporary directory structure and mocks paths for the manager.
    Returns the path to the mocked data directory.
    """
    
    # Create the necessary directories: data/ and src/
    data_dir = tmp_path / 'data'
    data_dir.mkdir()
    
    # Create the necessary file: assignments.json
    (data_dir / 'assignments.json').write_text("[]")
    
    # Mock os.path.dirname(__file__) to return a predictable location ('src/')
    mock_src_dir = str(tmp_path / 'src')
    
    # Patch the environment variables used by the AssignmentsManager for path resolution
    with patch('os.path.dirname', return_value=mock_src_dir):
        with patch('os.path.abspath', side_effect=lambda x: str(tmp_path) + '/' + x):
            return data_dir

@pytest.fixture
def AssignmentsManager(mock_path):
    """Imports and returns the AssignmentsManager class."""
    
    # Ensure the Assignment class used internally by TasksManager is the one from src/models.py
    # We must import the model first due to the sys.path modification trick in the manager file
    from src.models import Assignment
    
    # Temporarily adjust the Python path to import modules from src/
    import sys
    sys.path.insert(0, str(mock_path.parent))
    
    # Import the module under test and patch its internal model reference
    with patch('src.tasks_manager.Assignment', Assignment):
        from src.tasks_manager import AssignmentsManager
        
        # Clean up path
        sys.path.pop(0)
        
        return AssignmentsManager

@pytest.fixture
def am_instance(AssignmentsManager):
    """Provides a fresh instance of AssignmentsManager for each test."""
    return AssignmentsManager()

# --- Test Functions ---

def test_initialization_loads_and_sets_next_id(am_instance):
    """Tests that the manager correctly loads from an empty file and sets next_id."""
    assert len(am_instance.assignments) == 0
    assert am_instance.next_id == 1

def test_add_assignment_updates_and_persists(am_instance, mock_path):
    """Tests adding an assignment with all fields and verifying persistence."""
    
    new_assignment = am_instance.add_assignment(
        title="Physics Project", 
        course="PHY 101", 
        due_date="2025-12-10", 
        priority=5, 
        notes_markdown="Need to finish circuit diagram."
    )
    
    # 1. Assert internal state update
    assert len(am_instance.assignments) == 1
    assert new_assignment.priority == 5
    assert am_instance.next_id == 2
    
    # 2. Assert file persistence (check all fields, including the new ones)
    tasks_file = mock_path / 'assignments.json'
    data = json.loads(tasks_file.read_text())
    assert len(data) == 1
    assert data[0]['title'] == "Physics Project"
    assert data[0]['course'] == "PHY 101"
    assert data[0]['priority'] == 5
    assert data[0]['notes_markdown'].startswith("Need to finish")

def test_persistence_across_instances_and_next_id(AssignmentsManager, am_instance):
    """Tests if tasks added in one instance are available in a new instance."""
    
    # Instance A adds tasks
    am_instance.add_assignment("First Task", "CS", "2025-11-20", 3)
    am_instance.add_assignment("Second Task", "CS", "2025-11-21", 4)
        
    # Instance B loads tasks (new instance)
    tm_b = AssignmentsManager()
        
    # Assert tasks were loaded and next_id is correct
    assert len(tm_b.assignments) == 2
    assert tm_b.next_id == 3 # Should continue sequence

def test_complete_assignment_updates_status_and_saves(am_instance, mock_path):
    """Tests completing a task."""
    
    a1 = am_instance.add_assignment("Complete Me", "Math", "2025-11-20", 3)
    
    # Complete the assignment
    result = am_instance.complete_assignment(a1.id)
    assert result is True
    
    # Assert internal state update
    assert am_instance.assignments[0].status == "Complete"
    
    # Assert file persistence
    tasks_file = mock_path / 'assignments.json'
    data = json.loads(tasks_file.read_text())
    assert data[0]['status'] == "Complete"

def test_delete_assignment_removes_from_list_and_file_with_link_cleanup(am_instance, mock_path):
    """Tests deleting an assignment and verifies link cleanup (PKMS feature)."""
    
    # Create A, B, and C
    a1 = am_instance.add_assignment("Task A (Target)", "C", "2025-12-01", 3)
    a2 = am_instance.add_assignment("Task B (Source)", "C", "2025-12-05", 3)
    a3 = am_instance.add_assignment("Task C (Source)", "C", "2025-12-10", 3)
    
    # Link B -> A and C -> A
    am_instance.add_link(a2.id, a1.id)
    am_instance.add_link(a3.id, a1.id)
    
    # DELETE Task A (the target)
    am_instance.delete_assignment(a1.id)
    
    # 1. Assert internal state update
    assert len(am_instance.assignments) == 2
    
    # 2. Assert link cleanup in remaining tasks (B and C)
    task_b = am_instance.get_assignment(a2.id)
    task_c = am_instance.get_assignment(a3.id)
    
    assert task_b.linked_ids == [] # Link removed
    assert task_c.linked_ids == [] # Link removed
    
    # 3. Assert file persistence
    tasks_file = mock_path / 'assignments.json'
    data = json.loads(tasks_file.read_text())
    assert len(data) == 2
    assert 'linked_ids' in data[0]
    assert data[0]['linked_ids'] == []
    
def test_list_assignments_is_sorted_by_due_date(am_instance):
    """Tests that assignments are sorted by due date, earliest first."""
    
    am_instance.add_assignment("Latest", "X", "2025-12-30", 3)
    am_instance.add_assignment("Earliest", "X", "2025-12-01", 3)
    am_instance.add_assignment("Middle", "X", "2025-12-15", 3)
    
    sorted_list = am_instance.list_assignments()
    
    assert sorted_list[0].title == "Earliest"
    assert sorted_list[1].title == "Middle"
    assert sorted_list[2].title == "Latest"

def test_add_link_functionality(am_instance):
    """Tests the PKMS linking feature."""
    
    a1 = am_instance.add_assignment("Source", "X", "2025-12-01", 3)
    a2 = am_instance.add_assignment("Target 1", "Y", "2025-12-05", 3)
    a3 = am_instance.add_assignment("Target 2", "Z", "2025-12-10", 3)
    
    # Add link 1 -> 2
    assert am_instance.add_link(a1.id, a2.id) is True
    assert a1.linked_ids == [a2.id]
    
    # Add link 1 -> 3
    assert am_instance.add_link(a1.id, a3.id) is True
    assert a1.linked_ids == [a2.id, a3.id]

    # Attempt to link to self (should fail)
    assert am_instance.add_link(a1.id, a a.id) is False
    
    # Attempt to add duplicate link (should not change the list)
    am_instance.add_link(a1.id, a2.id)
    assert a1.linked_ids == [a2.id, a3.id]

def test_get_linked_titles_retrieves_correct_data(am_instance):
    """Tests retrieval of linked titles and IDs."""
    
    a1 = am_instance.add_assignment("Source Report", "A", "2025-12-01", 3)
    a2 = am_instance.add_assignment("Draft 1", "A", "2025-12-05", 3)
    a3 = am_instance.add_assignment("Supporting Note", "B", "2025-12-10", 3)
    
    am_instance.add_link(a1.id, a2.id)
    am_instance.add_link(a1.id, a3.id)
    
    linked_titles = am_instance.get_linked_titles(a1.id)
    
    expected = [
        {"id": a2.id, "title": "Draft 1"},
        {"id": a3.id, "title": "Supporting Note"},
    ]
    
    assert linked_titles == expected

def test_priority_validation_on_model_init():
    """Tests that the Assignment model raises an error for invalid priority."""
    from src.models import Assignment
    
    # Test valid priority
    Assignment(1, "Valid", "C", "2025-01-01", 3)
    
    # Test low invalid priority
    with pytest.raises(ValueError, match="Priority must be between 1 and 5."):
        Assignment(1, "Invalid Low", "C", "2025-01-01", 0)

    # Test high invalid priority
    with pytest.raises(ValueError, match="Priority must be between 1 and 5."):
        Assignment(1, "Invalid High", "C", "2025-01-01
