import uuid
from datetime import datetime
from typing import Optional, List, Dict, Any

class KnowledgeEntry:
    """Represents a piece of PKMS knowledge."""
    def __init__(self, title: str, content: str, tags: Optional[List[str]] = None,
                 id: Optional[str] = None, created_at: Optional[str] = None,
                 summary: Optional[str] = None, is_summarized: bool = False):
        
        self.id = id if id is not None else str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags if tags is not None else []
        self.created_at = created_at if created_at is not None else datetime.now().isoformat()
        self.summary = summary
        self.is_summarized = is_summarized

    def to_dict(self) -> Dict[str, Any]:
        """Converts the object to a dictionary for JSON serialization."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'KnowledgeEntry':
        """Creates an object from a dictionary (JSON deserialization)."""
        return cls(
            id=data.get('id'),
            title=data['title'],
            content=data['content'],
            tags=data.get('tags'),
            created_at=data.get('created_at'),
            summary=data.get('summary'),
            is_summarized=data.get('is_summarized', False)
        )

class Task:
    """Represents a personal task."""
    def __init__(self, title: str, description: str, due_date: str,
                 knowledge_link_id: Optional[str] = None, id: Optional[str] = None,
                 created_at: Optional[str] = None, status: str = "pending",
                 priority: str = "medium", is_prioritized: bool = False):
        
        self.id = id if id is not None else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date # YYYY-MM-DD string
        self.status = status
        self.priority = priority
        self.knowledge_link_id = knowledge_link_id
        self.created_at = created_at if created_at is not None else datetime.now().isoformat()
        self.is_prioritized = is_prioritized

    def to_dict(self) -> Dict[str, Any]:
        """Converts the object to a dictionary for JSON serialization."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Creates an object from a dictionary (JSON deserialization)."""
        return cls(
            id=data.get('id'),
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            knowledge_link_id=data.get('knowledge_link_id'),
            created_at=data.get('created_at'),
            status=data.get('status', 'pending'),
            priority=data.get('priority', 'medium'),
            is_prioritized=data.get('is_prioritized', False)
        )
