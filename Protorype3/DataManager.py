import json
import os
import uuid
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

    @staticmethod
    def save_data(filepath, data):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

class KnowledgeEntry:
    def __init__(self, title, content, tags=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        self.created_at = datetime.now().isoformat()
        self.summary = None
        self.is_summarized = False # New state for agent
    
    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        entry = cls(data['title'], data['content'], data.get('tags'))
        entry.id = data.get('id')
        entry.created_at = data.get('created_at')
        entry.summary = data.get('summary')
        # Check if summary exists to infer if it has been processed
        entry.is_summarized = bool(data.get('summary'))
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
        self.is_prioritized = False # New state for agent
    
    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        task = cls(data['title'], data['description'], data['due_date'], data.get('knowledge_link_id'))
        task.id = data.get('id')
        task.status = data.get('status')
        task.priority = data.get('priority')
        task.created_at = data.get('created_at')
        # Check if priority is one of the initial defaults to infer if it has been processed
        task.is_prioritized = task.priority.lower() not in ["medium"] 
        return task

# --- Mock LLM Function (Simulates API Interaction) ---

def mock_llm_call(prompt, task="summarize"):
    """
    Mocks an API call to a Large Language Model.
    In a real application, this would use a library like 'requests'
    to communicate with a service like Gemini, OpenAI, etc.
    """
    print(f"\n[MOCK LLM] Processing {task}...")
    
    if task == "summarize":
        # Simple, deterministic summary based on input length
        return f"A concise AI summary: This entry covers important points related to {prompt.split()[2]} and contains {len(prompt)} characters of original data."
    
    elif task == "prioritize":
        # Simple logic to determine priority based on keywords/length
        if "deadline" in prompt.lower() or "critical" in prompt.lower() or "due date" in prompt.lower():
            return "high"
        elif len(prompt) > 300:
            return "medium"
        else:
            return "low"
    
    return "Error: Unknown task"


class AIAgent:
    """An AI agent to process knowledge and task data automatically."""
    def __init__(self):
        self.knowledge = [KnowledgeEntry.from_dict(d) for d in DataManager.load_data(PKM_FILE)]
        self.tasks = [Task.from_dict(d) for d in DataManager.load_data(TASK_FILE)]
        self.knowledge_updated = False
        self.tasks_updated = False
        print(f"AI Agent Initialized. Loaded {len(self.knowledge)} knowledge entries and {len(self.tasks)} tasks.")

    def summarize_new_entries(self):
        """Finds knowledge entries without a summary and generates one."""
        new_entries = [e for e in self.knowledge if not e.is_summarized]
        
        if not new_entries:
            print("No new knowledge entries found for summarization.")
            return

        print(f"\n--- Starting AI Summarization for {len(new_entries)} entries ---")
        
        for entry in new_entries:
            # Prepare content for the LLM call
            content_to_summarize = f"Title: {entry.title}\nContent: {entry.content}"
            
            # Simulate LLM call
            summary_text = mock_llm_call(content_to_summarize, task="summarize")
            
            # Update the entry object
            entry.summary = summary_text
            entry.is_summarized = True
            self.knowledge_updated = True
            print(f"[SUCCESS] Summarized '{entry.title}'.")
            
    def prioritize_tasks(self):
        """Analyzes pending tasks and assigns a priority."""
        pending_tasks = [t for t in self.tasks if t.status == "pending" and not t.is_prioritized]
        
        if not pending_tasks:
            print("No new or unprioritized pending tasks found.")
            return

        print(f"\n--- Starting AI Task Prioritization for {len(pending_tasks)} tasks ---")

        for task in pending_tasks:
            # Gather context for the LLM: task description + linked knowledge content
            context = task.description
            if task.knowledge_link_id:
                linked_entry = next((e for e in self.knowledge if e.id == task.knowledge_link_id), None)
                if linked_entry:
                    context += f" [Linked Knowledge: {linked_entry.title} - {linked_entry.summary or linked_entry.content[:100]}...]"

            # Simulate LLM call to get structured priority
            new_priority = mock_llm_call(context, task="prioritize")
            
            # Update the task object
            task.priority = new_priority
            task.is_prioritized = True
            self.tasks_updated = True
            print(f"[SUCCESS] Prioritized '{task.title}' to '{new_priority.upper()}'.")

    def run(self):
        """Runs the agent's full processing cycle."""
        print("\n==============================================")
        print("     PKMS AI Agent - Processing Cycle Start   ")
        print("==============================================")
        
        self.summarize_new_entries()
        self.prioritize_tasks()
        
        print("\n--- Saving Changes ---")
        if self.knowledge_updated:
            DataManager.save_data(PKM_FILE, [e.to_dict() for e in self.knowledge])
            print("Knowledge data saved.")
        if self.tasks_updated:
            DataManager.save_data(TASK_FILE, [t.to_dict() for t in self.tasks])
            print("Task data saved.")
            
        print("\nAgent cycle complete.")
        print("==============================================")


if __name__ == "__main__":
    # Note: Run pkm_core.py first to ensure data files exist.
    # The agent uses 'is_summarized' and 'is_prioritized' flags to avoid reprocessing.
    agent = AIAgent()
    agent.run()
