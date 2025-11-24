import json
import os
import uuid
from datetime import datetime

# --- Configuration ---
PKM_FILE = "knowledge.json"
TASK_FILE = "tasks.json"

class DataManager:
    """Handles loading and saving data to JSON files."""
    @staticmethod
    def load_data(filepath):
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from {filepath}. Starting with empty list.")
            return []

    @staticmethod
    def save_data(filepath, data):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"\n--- Data saved successfully to {filepath} ---")

class KnowledgeEntry:
    """Represents a single piece of stored knowledge."""
    def __init__(self, title, content, tags=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        self.created_at = datetime.now().isoformat()
        self.summary = None # Placeholder for AI summarization

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        entry = cls(data['title'], data['content'], data.get('tags'))
        entry.id = data.get('id', str(uuid.uuid4()))
        entry.created_at = data.get('created_at', datetime.now().isoformat())
        entry.summary = data.get('summary')
        return entry

class Task:
    """Represents a personal task."""
    def __init__(self, title, description, due_date, knowledge_link_id=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "pending"
        self.priority = "medium" # Placeholder for AI prioritization
        self.knowledge_link_id = knowledge_link_id
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        task = cls(data['title'], data['description'], data['due_date'], data.get('knowledge_link_id'))
        task.id = data.get('id', str(uuid.uuid4()))
        task.status = data.get('status', "pending")
        task.priority = data.get('priority', "medium")
        task.created_at = data.get('created_at', datetime.now().isoformat())
        return task

class PKMSCore:
    """The main application logic for PKMS and Task Management."""
    def __init__(self):
        self.knowledge = [KnowledgeEntry.from_dict(d) for d in DataManager.load_data(PKM_FILE)]
        self.tasks = [Task.from_dict(d) for d in DataManager.load_data(TASK_FILE)]

    def add_knowledge_entry(self):
        title = input("Enter Title: ")
        content = input("Enter Content: ")
        tags_input = input("Enter Tags (comma-separated, optional): ")
        tags = [t.strip() for t in tags_input.split(',')] if tags_input else []
        entry = KnowledgeEntry(title, content, tags)
        self.knowledge.append(entry)
        print(f"\nKnowledge entry '{title}' added with ID: {entry.id}")

    def add_task(self):
        title = input("Enter Task Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        link_id = input("Link to Knowledge ID (optional): ") or None
        task = Task(title, description, due_date, link_id)
        self.tasks.append(task)
        print(f"\nTask '{title}' added with ID: {task.id}")

    def view_tasks(self, status="pending"):
        print(f"\n--- {status.upper()} TASKS ---")
        filtered = [t for t in self.tasks if t.status == status]
        if not filtered:
            print("No tasks found.")
            return
        for i, task in enumerate(filtered, 1):
            link = f" (Linked to {task.knowledge_link_id[:8]}...)" if task.knowledge_link_id else ""
            print(f"{i}. [{task.priority.upper()}] {task.title} (Due: {task.due_date}){link}")
            print(f"   Description: {task.description}")

    def mark_task_complete(self):
        self.view_tasks("pending")
        task_id = input("\nEnter ID of task to mark complete: ")
        for task in self.tasks:
            if task.id == task_id:
                task.status = "complete"
                print(f"Task '{task.title}' marked as complete.")
                return
        print("Error: Task ID not found.")

    def save_all(self):
        DataManager.save_data(PKM_FILE, [e.to_dict() for e in self.knowledge])
        DataManager.save_data(TASK_FILE, [t.to_dict() for t in self.tasks])

def main_core():
    app = PKMSCore()
    
    print("Welcome to the Core PKMS CLI.")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Knowledge Entry")
        print("2. Add Task")
        print("3. View Pending Tasks")
        print("4. Mark Task Complete")
        print("5. Save & Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            app.add_knowledge_entry()
        elif choice == '2':
            app.add_task()
        elif choice == '3':
            app.view_tasks("pending")
        elif choice == '4':
            app.mark_task_complete()
        elif choice == '5':
            app.save_all()
            print("Exiting application. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_core()
