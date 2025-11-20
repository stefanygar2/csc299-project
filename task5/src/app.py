import json
from datetime import datetime
from typing import List, Optional

class Assignment:
    """
    Represents a single student assignment item, including PKMS features.
    """
    def __init__(self, id: int, title: str, course: str, due_date: str, priority: int, 
                 notes_markdown: str = "", status: str = "Pending", linked_ids: Optional[List[int]] = None):
        
        self.id = id
        self.title = title
        self.course = course
        self.due_date = due_date # Stored as ISO string (YYYY-MM-DD)
        self.priority = priority # Integer 1 to 5
        self.notes_markdown = notes_markdown
        self.status = status     # "Pending" or "Complete"
        self.linked_ids = linked_ids if linked_ids is not None else []
        
        # Validation checks (optional, but good practice)
        if not 1 <= self.priority <= 5:
            raise ValueError("Priority must be between 1 and 5.")

    def complete(self):
        """Marks the assignment as completed."""
        self.status = "Complete"
        
    def add_link(self, target_id: int):
        """Adds a link to another assignment ID."""
        if target_id not in self.linked_ids:
            self.linked_ids.append(target_id)

    def to_dict(self):
        """Returns a serializable dictionary representation of the assignment."""
        return self.__dict__

    def __repr__(self):
        return (f"Assignment(id={self.id}, title='{self.title}', course='{self.course}', "
                f"due_date='{self.due_date}', priority={self.priority}, status='{self.status}', "
                f"links={len(self.linked_ids)})")

    def __eq__(self, other):
        if not isinstance(other, Assignment):
            return NotImplemented
        # Compare core fields for equality check
        return all([
            self.id == other.id, self.title == other.title, self.course == other.course, 
            self.due_date == other.due_date, self.priority == other.priority, 
            self.status == other.status, self.linked_ids == other.linked_ids
        ])
