# Integrated PKMS Task Manager (task6)

This repository contains the final, integrated prototype for a Personal Knowledge Management System (PKMS) and Task Manager. The application is built in portable Python (without external dependencies like Pydantic) and includes a Command Line Interface (CLI), JSON file persistence, and an integrated AI Agent for processing data.

Project Structure

The core application logic is contained within the task6 Python package.

finalpro/
├── pyproject.toml      # Project metadata, dependencies, and `uv` scripts
└── task6/
    ├── src/
    │   ├── __main__.py     # Main application logic (`PKMSTaskManager` class and CLI entry)
    │   ├── data_manager.py # Handles JSON file persistence (knowledge.json, tasks.json, schedule.json)
    │   ├── models.py       # Standard Python classes for data (Task, KnowledgeEntry, Schedule)
    │   └── llm_agent.py    # AI integration (OpenAI API Mock)
    └── tests/
        └── test_manager.py # Pytest unit tests

# Setup & Installation

The project uses uv for dependency management. Ensure you are in the directory containing pyproject.toml (finalpro) before running these commands.

Navigate to the project root:

```` cd finalpro ````


Create the virtual environment and install dependencies:

uv venv
uv pip install -e .


▶️ Execution

1. Run the CLI Application

To start the interactive menu, you must use the python -m command, which correctly executes the __main__.py file within the task6.src package.

# This is the most reliable way to execute the application
source .venv/bin/activate  # Optional, but recommended
python -m task6.src


2. Run the Unit Tests

This command executes the tests in task6/tests/test_manager.py.

uv run pytest


⚙️ Key Features

Data Management

All data is stored in the .data/ directory using simple JSON files: knowledge.json, tasks.json, and schedule.json.

CLI Menu Options

The CLI allows for direct interaction with all data types:

Option

Action

Data Type

1

Add Knowledge Entry

Stores notes, tags, and content.

2

Add Task

Stores tasks with due dates and optional links to knowledge entries.

3

List Pending Tasks

Displays tasks, sorted by AI-assigned priority.

4

Search Knowledge (PKM)

Performs keyword searches across entry titles and content.

6

Add Work Schedule

NEW: Records structured schedule commitments (Day, Time, Location).

7

Save & Exit

Saves all current knowledge, tasks, and schedules to JSON.

AI Agent Processing

Option 5, "Run AI Agent Cycle," executes background logic that uses a mocked LLM (Large Language Model) to automatically process your data:

Summarization: Generates and saves a short summary for any new KnowledgeEntry that lacks one.

Prioritization: Assigns a priority (high, medium, or low) to any new pending Task based on keywords in its description and linked knowledge.
