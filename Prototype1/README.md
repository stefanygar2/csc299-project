📋 Prototype 1: Core PKMS and Task Manager (pkm_core.py)

This is the foundational prototype, providing a basic Command Line Interface (CLI) for managing Personal Knowledge Entries and Tasks. It handles all data persistence using simple JSON files, ensuring maximum portability.

# ✨ Features

Knowledge Management: Create, store, and tag detailed knowledge entries.

Task Management: Add tasks with due dates and link them to knowledge entries.

Persistent Storage: All data is saved automatically to local JSON files.

CLI Interface: Simple, menu-driven interface for core operations.

# 🚀 Setup & Execution

Since this script uses only Python's standard library, no external packages are required.

Ensure Python is installed: (Python 3.6+ recommended)

Run the script:

python pkm_core.py


# 💾 Data Files

The script automatically creates and manages two JSON files in the same directory:

Filepath

Description

knowledge.json

Stores all KnowledgeEntry objects, including content, tags, and summary placeholders.

tasks.json

Stores all Task objects, including status, priority, and links to knowledge entries.

# 📝 Usage Guide

When you run the script, a main menu will appear:

Add Knowledge Entry: Prompts you for a title, content, and comma-separated tags.

Add Task: Prompts for a title, description, due date (YYYY-MM-DD), and an optional ID to link it to an existing knowledge entry.

View Pending Tasks: Lists all tasks currently marked as "pending".

Mark Task Complete: Allows you to change a task's status from "pending" to "complete" using its unique ID.

Save & Exit: Saves all current data back to the JSON files before closing the application.
