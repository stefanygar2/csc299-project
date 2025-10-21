This is a simple command-line application built in Python for storing, listing, and searching tasks. Data is persisted in a local JSON file (tasks.json).
# Prerequisites
Python 3.8+

# Setup and Installation

Follow these steps to set up and run the application in a portable virtual environment.
Navigate to the tasks1 directory:

cd csc299-project/tasks1
Copy this into terminal 

Create environment- python -m venv venv

Activate environment - source venv/bin/activate
Run the Application-python task_cli.py
# Usage 
Once running, the application will prompt you for commands.

add --> add <Task Title> --> Creates a new task. You will be prompted for a priority (1-5).

Example :add Review chapter 5 notes

done -->done <Task ID> --> Marks a task as 'DONE'.--> 
Example:done 2

delete-->delete <Task ID>--> Permanently removes a task by its ID.

Example: delete 4

list-->list-->Displays all stored tasks in a plain formatted list, sorted by priority.

Example: list

search-->search <Keyword>--> Finds and displays tasks where the title contains the specified keyword
Example: search review

quit--> quit--> Exits the application.

quit

Data Storage

All task data is automatically stored in a file named tasks.json in the same directory.
