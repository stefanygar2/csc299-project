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
    
def mark_done(tasks: list, task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == 'DONE':
                print(f"\n[INFO] Task ID {task_id} is already marked DONE.")
                return
            task['status'] = 'DONE'
            save_tasks(tasks)
            print(f"\n[SUCCESS] Task ID {task_id} marked as DONE. Well done!")
            return
    print(f"\n[ERROR] Task with ID {task_id} not found.")

def delete_task(tasks: list, task_id: int):
    initial_length = len(tasks)
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) < initial_length:
        save_tasks(tasks)
        print(f"\n[SUCCESS] Task ID {task_id} permanently deleted.")
    else:
        print(f"\n[ERROR] Task with ID {task_id} not found.")

def main():
    tasks = load_tasks()

    print_header("JSON-Based Task Manager CLI")
    print("Manage your tasks stored in 'tasks.json'.")

    while True:
        try:
            command_parts = input("\nCommand (add/list/done/delete/search/quit) > ").strip().lower().split(' ', 1)
            
            if not command_parts:
                continue
            action=command_parts[0]
            arguments=command_parts[1:]
            
            if action == 'quit':
                print("\n[INFO] Application shutting down. Goodbye!")
                break
            
            elif action == 'add':
                if arguments:
                    # Reconstruct title from arguments
                    title = " ".join(arguments).strip() 
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
            
            elif action == 'done':
                if arguments and arguments[0].isdigit():
                    task_id = int(arguments[0])
                    mark_done(tasks, task_id)
                else:
                    print("[ERROR] Usage: done <Task ID>")

            elif action == 'delete':
                if arguments and arguments[0].isdigit():
                    task_id = int(arguments[0])
                    delete_task(tasks, task_id)
                else:
                    print("[ERROR] Usage: delete <Task ID>")

            elif action == 'search':
                if arguments:
                    keyword = " ".join(arguments).strip()
                    search_tasks(tasks, keyword)
                else:
                    print("[ERROR] Usage: search <Keyword>")

            else:
                print(f"[ERROR] Unknown command: '{action}'. Type 'quit' to exit.")

        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")
                

if __name__ == "__main__":
    main()
