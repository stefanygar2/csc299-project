import json
import os
import uuid
import re
from datetime import datetime

# --- Configuration (Reused from Core) ---
PKM_FILE = "knowledge.json"
TASK_FILE = "tasks.json"

# --- Data Structures (Reused from Core) ---
class DataManager:
    """Handles loading and saving data to JSON files."""
    @staticmethod
    def load_data(filepath):
        if not os.path.exists(filepath): return []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

class KnowledgeEntry:
    def __init__(self, title, content, tags=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        self.created_at = datetime.now().isoformat()
        self.summary = None
    
    @classmethod
    def from_dict(cls, data):
        entry = cls(data['title'], data['content'], data.get('tags'))
        entry.id = data.get('id')
        entry.created_at = data.get('created_at')
        entry.summary = data.get('summary')
        return entry

class Task:
    def __init__(self, title, description, due_date, knowledge_link_id=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "pending"
        self.priority = "medium"
        self.knowledge_link_id = knowledge_link_id
        self.created_at = datetime.now().isoformat()
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data['title'], data['description'], data['due_date'], data.get('knowledge_link_id'))
        task.id = data.get('id')
        task.status = data.get('status')
        task.priority = data.get('priority')
        task.created_at = data.get('created_at')
        return task

class PKMSChat:
    """A terminal-based chat interface for querying PKMS data."""
    def __init__(self):
        self.knowledge = [KnowledgeEntry.from_dict(d) for d in DataManager.load_data(PKM_FILE)]
        self.tasks = [Task.from_dict(d) for d in DataManager.load_data(TASK_FILE)]
        print(f"PKMS Chat Engine Initialized.")
        print(f"Loaded {len(self.knowledge)} knowledge entries and {len(self.tasks)} tasks.")

    def _format_knowledge_entry(self, entry):
        tags_str = ", ".join(entry.tags)
        return (
            f"--- Knowledge ID: {entry.id[:8]}... ---\n"
            f"Title: {entry.title}\n"
            f"Tags: {tags_str}\n"
            f"Content Summary: {entry.summary if entry.summary else entry.content[:150] + '...'}\n"
        )

    def _format_task(self, task):
        return (
            f"--- Task ID: {task.id[:8]}... ---\n"
            f"Title: {task.title}\n"
            f"Status: {task.status.upper()} (Priority: {task.priority.upper()})\n"
            f"Due: {task.due_date}\n"
            f"Description: {task.description}\n"
        )

    def process_query(self, query):
        """Processes a natural language query against PKMS data."""
        query_lower = query.lower()
        keywords = re.findall(r'\w+', query_lower)
        
        # 1. Check for Task-related intent
        if any(k in query_lower for k in ["task", "todo", "due", "priority", "complete"]):
            # Filter for task matches
            if "pending" in query_lower or "open" in query_lower:
                target_status = "pending"
            elif "complete" in query_lower:
                target_status = "complete"
            else:
                target_status = "pending" # Default to pending
            
            # Simple keyword matching on task fields
            task_results = []
            for t in self.tasks:
                if t.status == target_status:
                    if any(k in t.title.lower() or k in t.description.lower() for k in keywords):
                        task_results.append(t)
            
            if task_results:
                response = f"I found {len(task_results)} {target_status} task(s) matching your query:\n"
                response += "\n---\n".join([self._format_task(t) for t in task_results])
                return response
            else:
                return f"I couldn't find any {target_status} tasks matching those keywords. Try a broader search."

        # 2. Check for Knowledge-related intent (Default)
        
        # Simple keyword matching on knowledge fields and tags
        knowledge_results = []
        for e in self.knowledge:
            text_to_search = e.title.lower() + " " + e.content.lower() + " " + " ".join(e.tags).lower()
            if any(k in text_to_search for k in keywords):
                knowledge_results.append(e)

        if knowledge_results:
            response = f"I found {len(knowledge_results)} knowledge entry/entries relevant to your query:\n"
            response += "\n---\n".join([self._format_knowledge_entry(e) for e in knowledge_results])
            return response
        
        # 3. Default/Fallback response
        return "I'm sorry, I couldn't find any matching tasks or knowledge entries. Try asking about a tag, title, or topic."

    def run(self):
        print("\n==============================================")
        print("  PKMS Chat Interface (Type 'exit' to quit)   ")
        print("==============================================")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    print("PKMS Chat shutting down. Goodbye!")
                    break
                
                response = self.process_query(user_input)
                print("\nAssistant: " + response)
                
            except EOFError:
                print("\nPKMS Chat shutting down. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Note: For testing, ensure knowledge.json and tasks.json exist and have data
    # (Use pkm_core.py first to populate them, or create mock files.)
    chat_app = PKMSChat()
    chat_app.run()
