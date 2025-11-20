import json
import os
import datetime
from tasks3 import (
    load_data, save_data, get_next_id, 
    add_task, mark_done, delete_task
)
import pytest

# --- Test Fixtures and Setup ---

# Define temporary file paths for testing
TEST_TASK_FILE = 'test_tasks.json'

@pytest.fixture(autouse=True)
def setup_teardown(monkeypatch):
    """
    Sets up the testing environment by patching file paths 
    and ensuring test files are cleaned up.
    """
    # 1. Patch the global TASK_FILE variable in the imported module
    monkeypatch.setattr('tasks3.TASK_FILE', TEST_TASK_FILE)
    
    # 2. Yield control to the tests
    yield
    
    # 3. Teardown: Clean up the test file after each test
    if os.path.exists(TEST_TASK_FILE):
        os.remove(TEST_TASK_FILE)


# --- Utility Function Tests ---

def test_load_data_empty_file():
    """Test loading data from a non-existent or empty file."""
    assert load_data(TEST_TASK_FILE) == []

def test_save_and_load_data():
    """Test saving data to a file and successfully loading it back."""
    test_data = [{'id': 1, 'title': 'Test Item'}]
    save_data(TEST_TASK_FILE, test_data)
    loaded_data = load_data(TEST_TASK_FILE)
    assert loaded_data == test_data

def test_get_next_id_empty():
    """Test getting the next ID for an empty list."""
    assert get_next_id([]) == 1

def test_get_next_id_populated():
    """Test getting the next ID for a list with existing IDs."""
    data = [{'id': 5, 'title': 'A'}, {'id': 10, 'title': 'B'}]
    assert get_next_id(data) == 11


# --- Task Management Tests ---

def test_add_task_basic(capsys):
    """Test adding a task and checking its content."""
    add_task("Test Task 1", 2, None)
    
    tasks = load_data(TEST_TASK_FILE)
    assert len(tasks) == 1
    assert tasks[0]['title'] == "Test Task 1"
    assert tasks[0]['priority'] == 2
    assert tasks[0]['status'] == 'TODO'
    
    # Check success message output
    captured = capsys.readouterr()
    assert "[SUCCESS] Task added: ID 1 - 'Test Task 1'" in captured.out

def test_add_task_with_due_date_and_priority():
    """Test adding a task with a valid due date and priority."""
    add_task("Dated Task", 1, "2030-01-01")
    
    tasks = load_data(TEST_TASK_FILE)
    assert tasks[0]['priority'] == 1
    assert tasks[0]['due_date'] == "2030-01-01"

def test_add_task_invalid_date(capsys):
    """Test adding a task with an invalid date format."""
    add_task("Bad Date Task", 3, "01/01/2030")
    
    tasks = load_data(TEST_TASK_FILE)
    assert tasks[0]['due_date'] is None
    
    # Check warning message output
    captured = capsys.readouterr()
    assert "[WARNING] Invalid due date format." in captured.out

def test_mark_done_success(capsys):
    """Test successfully marking an existing task as DONE."""
    # Setup: Add a task first
    add_task("Task to Complete", 3, None)
    
    # Action: Mark it done
    mark_done(1)
    
    # Verification
    tasks = load_data(TEST_TASK_FILE)
    assert tasks[0]['status'] == 'DONE'
    
    captured = capsys.readouterr()
    assert "[SUCCESS] Task ID 1 marked as DONE." in captured.out

def test_mark_done_not_found(capsys):
    """Test attempting to mark a non-existent task as done."""
    mark_done(99) # Task ID 99 does not exist
    
    captured = capsys.readouterr()
    assert "[ERROR] Task with ID 99 not found." in captured.out

def test_delete_task_success(capsys):
    """Test successfully deleting an existing task."""
    # Setup: Add two tasks
    add_task("Task to Keep", 3, None)
    add_task("Task to Delete", 3, None) # ID 2
    
    # Action: Delete task ID 2
    delete_task(2)
    
    # Verification
    tasks = load_data(TEST_TASK_FILE)
    assert len(tasks) == 1
    assert tasks[0]['id'] == 1
    
    captured = capsys.readouterr()
    assert "[SUCCESS] Task ID 2 permanently deleted." in captured.out

def test_delete_task_not_found(capsys):
    """Test attempting to delete a non-existent task."""
    delete_task(99) # Task ID 99 does not exist
    
    captured = capsys.readouterr()
    assert "[ERROR] Task with ID 99 not found." in captured.out
