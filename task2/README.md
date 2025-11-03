# Chat Discussion 
ADD a calendar and note section 
ADD a search note 

# HOW TO USE 
Use the readme.md from task1 and 
JSON-Based Task and PKMS CLI Prototype (tasks1)

This is a simple command-line application built in Python for managing both tasks and notes. It uses two local JSON files for persistence:

Tasks are persisted in tasks.json.

Notes (PKMS) are persisted in notes.json.

The application is non-interactive and is executed directly from the terminal using command-line arguments via the standard Python argparse module.

Prerequisites

Python 3.8+

No external Python packages are required.

Setup and Installation

Follow these steps to set up and run the application in a portable virtual environment.

Navigate to the tasks1 directory:

cd csc299-project/tasks1


Create and Activate a Virtual Environment (Recommended for Portability):

# Create environment
python -m venv venv

# Activate environment (Linux/macOS)
source venv/bin/activate

# Activate environment (Windows)
.\venv\Scripts\activate


Run the Application:

Execute the file directly with a command followed by its arguments. Use python task_cli.py --help for a list of all available top-level commands.

Usage

Use the command format: python task_cli.py <command> [arguments] [options]

Task Management Commands

Command

Usage

Description

Example

add

add "<Title>" [--priority <1-5>] [--due <YYYY-MM-DD>]

Creates a new task. The title must be in quotes if it contains spaces.

python task_cli.py add "Submit final design" --priority 1 --due 2025-11-20

list

list

Displays all stored tasks, sorted by priority and due date.

python task_cli.py list

calendar

calendar <YYYY-MM-DD>

Displays all tasks due on the specified date.

python task_cli.py calendar 2025-11-15

done

done <Task ID>

Marks a task as 'DONE'.

python task_cli.py done 1

delete

delete <Task ID>

Permanently removes a task by its ID.

python task_cli.py delete 3

search

search <Keyword>

Finds and displays tasks where the title contains the keyword.

python task_cli.py search report

PKMS (Notes) Management Commands

Command

Usage

Description

Example

add_note

add_note "<Title>" --content "<Text>" [--tags "<tag1>,<tag2>"]

Creates a new note. Title and Content should be in quotes.

python task_cli.py add_note "ReAct Pattern" --content "Reasoning/Action loop for AI." --tags "AI, Agent"

search_note

search_note <Keyword>

Finds and displays notes by keyword (in title, content, or tags).

python task_cli.py search_note loop

Data Storage

Task data is stored in tasks.json.

Note data is stored in notes.json.
