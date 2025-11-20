import json
import os
import sys
from typing import List, Dict, Any, Optional
from datetime import datetime

# --- FIX: Handling the import error for direct execution ---
try:
    # Attempt the package-relative import first (preferred when imported)
    from .models import Assignment 
except ImportError:
    # If running the file directly (as a script), adjust sys.path to find models.py
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    # Assuming 'task5' is the package root and 'src' is inside it
    from src.models import Assignment
    
# -----------------------------------------------------------

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
TASKS_FILE = os.path.join(DATA_DIR, 'assignments.json') # Renamed file

class AssignmentsManager:
    """Manages the persistence and state of student assignments."""

    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'w') as f:
                f.write("[]")
        
        self.assignments: List[Assignment] = self._load_assignments()
        self.next_id = max([a.id for a in self.assignments], default=0) + 1

    def _load_assignments(self) -> List[Assignment]:
        """Loads assignments from the JSON file and converts them back to Assignment objects."""
        with open(TASKS_FILE, 'r') as f:
            data = json.load(f)
        
        loaded_assignments = []
        for d in data:
            # Instantiate Assignment using kwargs from the loaded dictionary
            try:
                # Ensure linked_ids are integers on load
                if 'linked_ids' in d and d['linked_ids'] is not None:
                     d['linked_ids'] = [int(i) for i in d['linked_ids']]
                loaded_assignments.append(Assignment(**d))
            except (ValueError, TypeError) as e:
                # Catch potential errors from bad data types on load
                print(f"Error loading assignment data {d}: {e}")
                continue 
                
        return loaded_assignments

    def _save_assignments(self):
        """Saves the current list of Assignment objects back to the JSON file."""
        with open(TASKS_FILE, 'w') as f:
            # Use the .to_dict() method to ensure data is serializable
            json.dump([a.to_dict() for a in self.assignments], f, indent=4)

    def add_assignment(self, title: str, course: str, due_date: str, priority: int, 
                       notes_markdown: str = "") -> Assignment:
        """
        Adds a new assignment with full details, validates priority, and saves.
        """
        new_assignment = Assignment(
            id=self.next_id,
            title=title,
            course=course,
            due_date=due_date,
            priority=priority,
            notes_markdown=notes_markdown
        )
        self.assignments.append(new_assignment)
        self.next_id += 1
        self._save_assignments()
        return new_assignment

    def list_assignments(self) -> List[Assignment]:
        """Returns all assignments, sorted by due date (ascending) for predictable output."""
        return sorted(self.assignments, key=lambda a: datetime.fromisoformat(a.due_date))

    def complete_assignment(self, id: int) -> bool:
        """Marks an assignment as completed."""
        for a in self.assignments:
            if a.id == id:
                a.complete()
                self._save_assignments()
                return True
        return False

    def delete_assignment(self, id: int):
        """Deletes an assignment and also cleans up any links pointing to it."""
        
        # 1. Remove the target assignment
        self.assignments = [a for a in self.assignments if a.id != id]
        
        # 2. Remove links pointing to the deleted ID (PKMS cleanup)
        for a in self.assignments:
            if id in a.linked_ids:
                a.linked_ids.remove(id)
                
        self._save_assignments()

    def add_link(self, source_id: int, target_id: int) -> bool:
        """PKMS Feature: Creates a link from source_id to target_id."""
        source_assignment = next((a for a in self.assignments if a.id == source_id), None)
        target_assignment = next((a for a in self.assignments if a.id == target_id), None)
        
        if source_assignment and target_assignment and source_id != target_id:
            source_assignment.add_link(target_id)
            self._save_assignments()
            return True
        return False

    def get_assignment(self, id: int) -> Optional[Assignment]:
        """Retrieves a single assignment by ID."""
        return next((a for a in self.assignments if a.id == id), None)

    def get_linked_titles(self, assignment_id: int) -> List[Dict[str, Any]]:
        """Retrieves ID and title of all assignments linked to the given ID."""
        assignment = self.get_assignment(assignment_id)
        if not assignment:
            return []
            
        linked_info = []
        for target_id in assignment.linked_ids:
            target_assignment = self.get_assignment(target_id)
            if target_assignment:
                linked_info.append({
                    "id": target_assignment.id,
                    "title": target_assignment.title
                })
        return linked_info

if __name__ == "__main__":
    # Example usage for testing purposes
    print("--- Testing AssignmentsManager ---")
    
    # Ensure a clean slate for the test
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)

    tm = AssignmentsManager()
    
    # Add assignments
    a1 = tm.add_assignment("Math HW 1", "Math 101", "2025-11-20", 4)
    a2 = tm.add_assignment("Essay Draft", "English 202", "2025-11-25", 5, notes_markdown="Start with intro.")
    a3 = tm.add_assignment("Final Exam Review", "Math 101", "2025-12-15", 3)
    
    print("\n--- List Initial Assignments (Sorted by Due Date) ---")
    for a in tm.list_assignments():
        print(f"ID {a.id}: {a.title} ({a.due_date})")
        
    # Test linking
    tm.add_link(a2.id, a1.id) # Link Essay Draft to Math HW 1
    
    print(f"\n--- Linked Tasks for Essay Draft (ID {a2.id}) ---")
    print(tm.get_linked_titles(a2.id))
    
    # Test completion
    tm.complete_assignment(a1.id)
    print(f"\nStatus of Math HW 1 (ID {a1.id}): {tm.get_assignment(a1.id).status}")
    
    # Test persistence (re-initialize manager)
    tm2 = AssignmentsManager()
    print(f"\nTasks in new instance (total: {len(tm2.assignments)}). Next ID is: {tm2.next_id}")
    print(f"Status of Math HW 1 in new instance: {tm2.get_assignment(a1.id).status}")
