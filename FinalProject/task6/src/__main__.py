import sys
import os
from typing import List

# Ensure local imports work regardless of execution context
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Imports use single-dot relative paths as they are still siblings in 'src'
from .models import Task, KnowledgeEntry, Schedule
from .data_manager import DataManager
from .llm_agent import LLMAgent

class PKMSTaskManager:
    """
    The main Personal Knowledge Management and Task Manager class.
    (This is the "spec-kit" class requested by the user).
    """
    def __init__(self):
        self.data_manager = DataManager()
        self.llm_agent = LLMAgent()
        self.knowledge: List[KnowledgeEntry] = self.data_manager.load_data(KnowledgeEntry, 'pkm')
        self.tasks: List[Task] = self.data_manager.load_data(Task, 'task')
        self.schedules: List[Schedule] = self.data_manager.load_data(Schedule, 'schedule') 
        print(f"Manager initialized. Loaded {len(self.knowledge)} knowledge entries, {len(self.tasks)} tasks, and {len(self.schedules)} schedules.")

    # --- CRUD Operations ---

    def add_knowledge_entry(self):
        title = input("Enter Title: ")
        content = input("Enter Content: ")
        tags_input = input("Enter Tags (comma-separated, optional): ")
        tags = [t.strip() for t in tags_input.split(',')] if tags_input else []
        entry = KnowledgeEntry(title=title, content=content, tags=tags)
        self.knowledge.append(entry)
        print(f"Knowledge entry '{title}' added with ID: {entry.id}")
    
    def add_task(self):
        title = input("Enter Task Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        
        if self.knowledge:
            print("\nAvailable Knowledge Entries for Linking:")
            for i, entry in enumerate(self.knowledge, 1):
                print(f"  {i}. {entry.title} (ID: {entry.id[:8]}...)")
        
            link_choice = input("Enter ID or number to link (or leave blank): ")
            link_id = None
            if link_choice:
                try:
                    index = int(link_choice) - 1
                    if 0 <= index < len(self.knowledge):
                        link_id = self.knowledge[index].id
                    else:
                        print("Invalid index. Linking by ID...")
                except ValueError:
                    linked_entry = next((e for e in self.knowledge if e.id.startswith(link_choice)), None)
                    if linked_entry:
                        link_id = linked_entry.id
                    else:
                        print("No matching Knowledge ID found.")
        else:
            link_id = None

        task = Task(title=title, description=description, due_date=due_date, knowledge_link_id=link_id)
        self.tasks.append(task)
        print(f"\nTask '{title}' added with ID: {task.id}. Priority: {task.priority}")
    
    def add_work_schedule(self): 
        print("\n--- Add New Schedule Entry ---")
        title = input("Enter Schedule Title (e.g., Weekly Team Meeting): ")
        day = input("Enter Day of Week (e.g., Monday): ")
        start_time = input("Enter Start Time (HH:MM format, e.g., 09:00): ")
        end_time = input("Enter End Time (HH:MM format, e.g., 17:00): ")
        location = input("Enter Location/Platform (optional): ") or None

        schedule = Schedule(
            title=title,
            day_of_week=day,
            start_time=start_time,
            end_time=end_time,
            location=location
        )
        self.schedules.append(schedule)
        print(f"\nSchedule '{title}' on {day} added successfully.")

    def complete_task(self): # <-- NEW METHOD: Complete Task
        pending_tasks = [t for t in self.tasks if t.status == "pending"]
        
        if not pending_tasks:
            print("\nNo pending tasks to complete.")
            return

        print("\n--- Pending Tasks (Enter ID to Complete) ---")
        for i, task in enumerate(pending_tasks, 1):
            priority_tag = f"[{task.priority.upper()}]".ljust(9) 
            print(f"{i}. {priority_tag} {task.title} (ID: {task.id[:8]}...)")
            
        task_id_prefix = input("Enter the full or first few chars of the Task ID to mark complete: ")
        
        found = False
        for task in self.tasks:
            if task.id.startswith(task_id_prefix) and task.status == "pending":
                task.status = "complete"
                print(f"\nTask '{task.title}' marked as COMPLETE.")
                found = True
                break
        
        if not found:
            print("Error: Could not find a pending task matching that ID.")

    # --- Retrieval and Display ---

    def list_tasks(self, status: str = "pending"):
        print(f"\n--- {status.upper()} TASKS ---")
        filtered_tasks = sorted(
            [t for t in self.tasks if t.status == status], 
            key=lambda t: t.priority, reverse=True
        )

        if not filtered_tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(filtered_tasks, 1):
            link = f" (Linked to {task.knowledge_link_id[:8]}...)" if task.knowledge_link_id else ""
            priority_tag = f"[{task.priority.upper()}]".ljust(9) 
            print(f"{i}. {priority_tag} {task.title} (Due: {task.due_date}){link}")
            print(f"   Description: {task.description}")

    def list_schedules(self):
        print("\n--- CURRENT WORK SCHEDULE ---")
        if not self.schedules:
            print("No schedules found.")
            return

        # Sort schedules by day of the week (simple alphabetical sort for prototype)
        sorted_schedules = sorted(self.schedules, key=lambda s: s.day_of_week)

        for i, schedule in enumerate(sorted_schedules, 1):
            time_slot = f"{schedule.start_time} - {schedule.end_time}"
            location_info = f" ({schedule.location})" if schedule.location else ""
            
            print(f"{i}. {schedule.day_of_week.ljust(10)} | {time_slot.ljust(15)} | {schedule.title}{location_info}")
            print("-" * 50)
            
    def search_pkm(self):
        query = input("Enter search keywords: ").lower()
        if not query:
            print("Please enter keywords.")
            return

        results = []
        for entry in self.knowledge:
            searchable_text = f"{entry.title} {entry.content} {' '.join(entry.tags)}".lower()
            if all(word in searchable_text for word in query.split()):
                results.append(entry)

        print(f"\n--- Found {len(results)} PKM results for '{query}' ---")
        if not results:
            return

        for i, entry in enumerate(results, 1):
            summary_display = entry.summary if entry.summary else entry.content[:100] + "..."
            print(f"{i}. [PKM Entry] Title: {entry.title}")
            print(f"   Summary: {summary_display}")
            print(f"   Tags: {', '.join(entry.tags)}")
            print(f"   ID: {entry.id}")

    # --- AI Agent Integration ---
    
    def run_agent_cycle(self):
        """Processes unsaved tasks and knowledge using the AI agent."""
        knowledge_updated = False
        tasks_updated = False
        
        print("\n==============================================")
        print("     PKMS AI Agent - Processing Cycle Start   ")
        print("==============================================")

        # 1. Summarize new knowledge entries
        new_entries = [e for e in self.knowledge if not e.is_summarized]
        print(f"AI: Found {len(new_entries)} entries to summarize.")
        for entry in new_entries:
            summary = self.llm_agent.summarize_entry(entry)
            entry.summary = summary
            entry.is_summarized = True
            knowledge_updated = True
            print(f"[SUMMARIZED] '{entry.title}'.")
        
        # 2. Prioritize tasks
        unprioritized_tasks = [t for t in self.tasks if t.status == "pending" and not t.is_prioritized]
        print(f"AI: Found {len(unprioritized_tasks)} pending tasks to prioritize.")
        for task in unprioritized_tasks:
            linked_content = ""
            if task.knowledge_link_id:
                linked = next((e for e in self.knowledge if e.id == task.knowledge_link_id), None)
                linked_content = linked.summary or linked.content if linked else "No linked content found."

            new_priority = self.llm_agent.prioritize_task(task, linked_content)
            task.priority = new_priority
            task.is_prioritized = True
            tasks_updated = True
            print(f"[PRIORITIZED] '{task.title}' to '{new_priority.upper()}'.")

        print("\nAgent cycle complete.")
        return knowledge_updated, tasks_updated

    def save_and_exit(self):
        """Saves all data before exiting."""
        self.data_manager.save_data(self.knowledge, 'pkm')
        self.data_manager.save_data(self.tasks, 'task')
        self.data_manager.save_data(self.schedules, 'schedule') 
        sys.exit(0)
    
    def run_cli(self):
        """The main CLI loop."""
        print("Welcome to the Integrated PKMS & Task Manager.")
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Knowledge Entry")
            print("2. Add Task")
            print("3. List Pending Tasks")
            print("4. Search Knowledge (PKM)")
            print("5. Run AI Agent Cycle (Summarize/Prioritize)")
            print("6. Add Work Schedule")
            print("7. List Work Schedules")
            print("8. Complete Task") # <-- NEW MENU ITEM
            print("9. Save & Exit") # <-- UPDATED OPTION
            

            choice = input("Select an option (1-9): ")
            
            try:
                if choice == '1':
                    self.add_knowledge_entry()
                elif choice == '2':
                    self.add_task()
                elif choice == '3':
                    self.list_tasks("pending")
                elif choice == '4':
                    self.search_pkm()
                elif choice == '5':
                    self.run_agent_cycle()
                elif choice == '6':
                    self.add_work_schedule() 
                elif choice == '7':
                    self.list_schedules()
                elif choice == '8':
                    self.complete_task() # <-- CALL NEW METHOD
                elif choice == '9':
                    self.save_and_exit()
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"\n[ERROR] An unexpected error occurred: {e}")

def main():
    """Entry point function for uv run task6."""
    manager = PKMSTaskManager()
    manager.run_cli()

if __name__ == "__main__":
