import copy
from typing import List, Dict, Optional, Union, Callable
import sys
import time # Needed for the placeholder summarize_text function

class ScheduleManager:
    def main():
     print("Hello from tasks4!")# proves it runs 
     if __name__ == "__main__":
         main()
    """
    Manages school and work schedule items, allowing adding, removing, 
    and displaying items.
    """
    def __init__(self) -> None:
        # Separate lists for school and work schedule items
        self.school_schedule: List[Dict] = []
        self.work_schedule: List[Dict] = []
        # Internal counter for generating unique IDs
        self._next_id: int = 1

    # ---------- Internal helpers ----------

    def _get_schedule_list(self, schedule_type: str) -> List[Dict]:
        """
        Return the internal list for a requested schedule_type.
        Valid values: 'school' or 'work' (case-insensitive).
        """
        if not isinstance(schedule_type, str):
            raise TypeError("schedule_type must be a string 'school' or 'work'.")
        st = schedule_type.lower()
        if st == "school":
            return self.school_schedule
        if st == "work":
            return self.work_schedule
        raise ValueError(f"Unknown schedule_type '{schedule_type}'. Use 'school' or 'work'.")

    def _generate_id(self) -> str:
        """Generate a simple unique id for items."""
        item_id = str(self._next_id)
        self._next_id += 1
        return item_id

    # ---------- Public methods ----------

    def add_item(self, schedule_type: str, title: str, time: Optional[str] = None, notes: Optional[str] = None) -> Dict:
        """
        Add a new item to the specified schedule and return the created item dict.
        """
        schedule = self._get_schedule_list(schedule_type)
        item = {
            "id": self._generate_id(),
            "title": title,
            "time": time,
            "notes": notes,
        }
        schedule.append(item)
        # Return a copy so external code can't mutate internal storage directly
        return copy.deepcopy(item)

    def remove_item(self, schedule_type: str, identifier: Union[int, str]) -> Dict:
        """
        Remove an item from schedule by index (int) or id (str) and return the removed item.

        Raises:
          - IndexError if index out of range
          - ValueError if id not found
          - TypeError if identifier type invalid
        """
        schedule = self._get_schedule_list(schedule_type)

        # Remove by integer index
        if isinstance(identifier, int):
            if identifier < 0 or identifier >= len(schedule):
                raise IndexError(f"Index {identifier} out of range for {schedule_type} schedule.")
            removed = schedule.pop(identifier)
            return copy.deepcopy(removed)

        # Remove by string id
        if isinstance(identifier, str):
            for idx, item in enumerate(schedule):
                if item.get("id") == identifier:
                    removed = schedule.pop(idx)
                    return copy.deepcopy(removed)
            raise ValueError(f"Item with id '{identifier}' not found in {schedule_type} schedule.")

        raise TypeError("Identifier must be an int (index) or str (id).")

    def display_schedule(self, schedule_type: Optional[str] = None) -> Union[Dict[str, List[Dict]], List[Dict]]:
        """
        Return schedule data (copies) for testing or display.
        """
        if schedule_type is None or (isinstance(schedule_type, str) and schedule_type.lower() == "both"):
            return {"school": copy.deepcopy(self.school_schedule), "work": copy.deepcopy(self.work_schedule)}
        schedule = self._get_schedule_list(schedule_type)
        return copy.deepcopy(schedule)

    def find_item(self, schedule_type: str, item_id: str) -> Optional[Dict]:
        """Find and return a copy of an item by id, or None if not found."""
        schedule = self._get_schedule_list(schedule_type)
        for item in schedule:
            if item.get("id") == item_id:
                return copy.deepcopy(item)
        return None

    def process_loop(self, callback: Callable[[Dict], None], schedule_type: Optional[str] = None) -> None:
        """
        Iterate over items in the requested schedule(s) and call callback(item) for each.
        The callback receives a copy of each item.
        """
        if schedule_type is None or (isinstance(schedule_type, str) and schedule_type.lower() == "both"):
            for item in copy.deepcopy(self.school_schedule):
                callback(item)
            for item in copy.deepcopy(self.work_schedule):
                callback(item)
            return

        schedule = self._get_schedule_list(schedule_type)
        for item in copy.deepcopy(schedule):
            callback(item)

    def interactive_menu(self) -> None:
        """
        Simple interactive menu. This uses input() and should NOT be called during automated tests.
        """
        print("Interactive menu. Type 'exit' at prompts to quit.")
        while True:
            print("\n1) Add item\n2) Remove item\n3) Display schedules\n4) Process items (demo)\n5) Exit")
            choice = input("Choose (1-5): ").strip()
            if choice == "5" or choice.lower() == "exit":
                print("Goodbye.")
                break
            if choice == "1":
                st = input("Schedule type ('school' or 'work'): ").strip()
                if st.lower() == "exit":
                    break
                title = input("Title: ").strip()
                time = input("Time (optional): ").strip() or None
                notes = input("Notes (optional): ").strip() or None
                try:
                    item = self.add_item(st, title, time, notes)
                    print("Added:", item)
                except Exception as exc:
                    print("Error:", exc)
            elif choice == "2":
                st = input("Schedule type ('school' or 'work'): ").strip()
                if st.lower() == "exit":
                    break
                ident = input("Identifier (index or id): ").strip()
                if ident.lower() == "exit":
                    break
                try:
                    key: Union[int, str]
                    if ident.isdigit():
                        key = int(ident)
                    else:
                        key = ident
                    removed = self.remove_item(st, key)
                    print("Removed:", removed)
                except Exception as exc:
                    print("Error:", exc)
            elif choice == "3":
                schedules = self.display_schedule()
                print("School:", schedules["school"])
                print("Work:", schedules["work"])
            elif choice == "4":
                def demo_cb(item: Dict) -> None:
                    print(f"Processing: {item['id']} - {item['title']}")
                self.process_loop(demo_cb)
            else:
                print("Invalid choice.")

# --- Placeholder Summarization Function ---

def summarize_text(description: str) -> str:
    """
    Conceptual function to simulate calling an LLM API to summarize text.
    (Simple placeholder logic for demonstration.)
    """
    time.sleep(0.05) # Simulate a brief processing delay
    
    lines = description.strip().split('\n')
    # Use the first non-empty line as a basic summary placeholder
    summary_phrase = lines[0].strip() if lines else "No content found."
    
    return f"Summary: '{summary_phrase}...'"

# Minimal non-interactive demo when run as a script
if __name__ == "__main__":
    # 1. ScheduleManager Demo (Original functionality)
    manager = ScheduleManager()
    manager.add_item("school", "Calculus Lecture", time="Mon 9:00", notes="Room 101")
    manager.add_item("school", "Group Project Meeting", time="Wed 14:00", notes="Online")
    manager.add_item("work", "Team Standup", time="Daily 10:00", notes="15 minutes")
    manager.add_item("work", "Client Presentation", time="Fri 15:00", notes="Prepare slides")

    print("--- 1. Schedule Manager Demo ---")
    all_schedules = manager.display_schedule()
    print("Current schedules:")
    print(all_schedules)

    print("\n" + "="*50 + "\n")
    
    # 2. Summarization Task (New functionality)
    print("--- 2. Batch Summarization Task ---")
    
    # Add at least 2 sample paragraph-length descriptions
    sample_descriptions = [
        # Sample 1: A complex work task description
        """
        The project review meeting for the new Q3 marketing initiative is scheduled for 
        Tuesday at 2 PM. Key stakeholders, including the VP of Marketing and the lead 
        development engineer, must be present. The purpose is to finalize the budget 
        allocation, review the pre-launch metrics from the soft-release trial, and assign 
        action items for the full product rollout on Friday. Ensure all financial reports 
        and metric dashboards are pre-loaded and accessible via the shared screen.
        """,
        
        # Sample 2: A detailed school assignment description
        """
        The final paper for the Comparative Literature course requires a minimum of 
        2,500 words and must analyze the thematic parallels between 'Don Quixote' and 
        'Moby Dick'. Students should focus specifically on the role of obsession and 
        the pursuit of unreachable ideals. References must be cited using MLA format. 
        The submission deadline is midnight on the 18th, and late submissions will incur 
        a 10% penalty per day.
        """
    ]
    
    # Add a loop to summarize multiple paragraph-length descriptions (independently of one another)
    for i, description in enumerate(sample_descriptions, 1):
        print(f"\nProcessing Description #{i}:")
        print(f"  Original Text Start: {description.strip()[:100]}...")
        
        # Summarize the current paragraph
        summary = summarize_text(description)
        
        # Print the independent summary
        print(f"  {summary}")

    print("\n--- Batch Summarization Complete ---")
    
    sys.exit(0)


    
