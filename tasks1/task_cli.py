import json
import os
from datetime import datetime
from typing import List, Dict, Any

TASK_FILE = 'tasks.json'

def print_header(text: str):
    print(f"\n--- {text.upper()} ---")

def print_separator():
    print("-" * 60)

def load_tasks() -> List[Dict[str, Any]]:
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("\n[Error] Task file is corrupted. Starting with an empty list.")
        return []

def save_tasks(tasks: List[Dict[str, Any]]):
    try:
        with open(TASK_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"\n[Error] Could not write to {TASK_FILE}. {e}")

def get_next_id(tasks: list) -> int:
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(tasks: list, title: str, priority: int = 3):
    new_id = get_next_id(tasks)
    new_task = {
        'id': new_id,
        'title': title,
        'status': 'TODO',
        'priority': priority,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\n[SUCCESS] Task added: ID {new_id} - '{title}'")

def list_tasks(tasks: list):
    if not tasks:
        print("\n[INFO] No tasks found. Add one using 'add'.")
        return

    print_header("Current Tasks")

    sorted_tasks = sorted(tasks, key=lambda t: t['priority'])

    print(f"{'ID':<4} | {'Prio':<5} | {'Title':<40} | {'Status':<10} | {'Created'}")
    print_separator()

    for task in sorted_tasks:
        
        try:
            created_time = datetime.fromisoformat(task['created_at']).strftime('%Y-%m-%d')
        except:
            created_time = "N/A"

        print(
            f"{task['id']:<4} | "
            f"{task['priority']:<5} | "
            f"{task['title'][:38]:<40} | "
            f"{task['status']:<10} | "
            f"{created_time}"
        )
    print_separator()

def search_tasks(tasks: list, keyword: str):
    keyword_lower = keyword.lower()
    results = [
        task for task in tasks
        if keyword_lower in task['title'].lower()
    ]

    if not results:
        print(f"\n[INFO] Search: No tasks matching '{keyword}' found.")
        return
    
    print_header(f"Search Results for '{keyword}'")
    list_tasks(results)

def main():
    tasks = load_tasks()

    print_header("JSON-Based Task Manager CLI")
    print("Manage your tasks stored in 'tasks.json'.")

    while True:
        try:
            command = input("\nCommand (add/list/search/quit) > ").strip().lower().split(' ', 1)
            action = command[0]
            
            if action == 'quit':
                print("\n[INFO] Application shutting down. Goodbye!")
                break
            
            elif action == 'add':
                if len(command) > 1 and command[1]:
                    title = command[1].strip()
                    priority_input = input("   Priority (1-5, default 3): ").strip() or '3'
                    try:
                        priority = int(priority_input)
                        if not 1 <= priority <= 5:
                            raise ValueError
                    except ValueError:
                        print("[ERROR] Invalid priority. Using default 3.")
                        priority = 3
                        
                    add_task(tasks, title, priority)
                else:
                    print("[ERROR] Usage: add <Task Title>")
            
            elif action == 'list':
                list_tasks(tasks)
            
            elif action == 'search':
                if len(command) > 1 and command[1].strip():
                    search_tasks(tasks, command[1].strip())
                else:
                    print("[ERROR] Usage: search <Keyword>")

            else:
                print(f"[ERROR] Unknown command: '{action}'. Type 'quit' to exit.")

        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
