# csc299-project
#Using Gemini 

# PROMPT
   I have to create a project for a csc class using python language that revolves around the use of AI coding  assistants to plan, specify, develop, and test your own software that includes:
personal knowledge management system (PKMS)
personal task management system
a terminal-based chat interface to interact with your stored knowledge and tasks
AI agents that interact with the stored knowledge or tasks , and must run portably on Windows, OSX, Linux. The state should be stored in JSON documents, a SQLite database, or a Neo4J database. Think about ideas for what the project can be 


# Output(Assiant):
That's a fantastic and challenging project assignment! I can definitely help you brainstorm some compelling project ideas that meet all your requirements, focusing on the seamless integration of PKMS, task management, and an AI agent in a terminal environment.

Here are three distinct project ideas—ranging from a professional focus to a more creative/academic focus—that fully satisfy the complexity and functionality requirements of your CSC class.

1. Project Idea: The Research Companion (Academia-Agent)
This idea focuses on supporting academic work, using the PKMS to store research snippets and the task manager to track reading and writing deadlines.
Component,Focus & Functionality
PKMS (Knowledge),"Stores Article Snippets, Definitions, and Source Citations. Each note includes a source_id (the paper it came from) and concept_tags (e.g., ""Deep Learning"", ""Ethical AI"")."
Task Management,"Tracks Reading Assignments (e.g., ""Read Chapter 3 by Friday""), Experiment Runs, and Drafting Deadlines. Priority is automatically assigned based on proximity to the due date."
Terminal Interface,"User types in queries like: task add ""Draft conclusion by 11/15"", or conversational queries for the AI."
AI Agent Core Skill,Synthesizing Evidence.
AI Agent Tools,"1. get_notes_by_tag(tag): Retrieves all notes related to a concept. 2. add_task(title, due_date): Creates a new deadline. 3. find_contradiction(concept_A, concept_B): Agent retrieves notes for both concepts and analyzes them for conflicting information."
Example AI Query,"""What evidence do I have on the limitations of large language models, and create a task for me to write a paragraph on it for next week."""
Data Storage,SQLite Database (Ideal for structured storage and quick retrieval of academic data).
I have to create a project for a csc class using python language that revolves around the use of AI coding  assistants to plan, specify, develop, and test your own software that includes:
personal knowledge management system (PKMS)
personal task management system
a terminal-based chat interface to interact with your stored knowledge and tasks
AI agents that interact with the stored knowledge or tasks , and must run portably on Windows, OSX, Linux. The state should be stored in JSON documents, a SQLite database, or a Neo4J database.
I can certainly help you structure this project. This is an excellent, modern project scope that touches on key concepts like database management, system design, and AI integration (specifically, the agent/tool-calling paradigm).

I recommend using Python's built-in sqlite3 module for state storage. It is the most portable option, requiring no external installation steps on Windows, OSX, or Linux, and it scales perfectly for a personal system.

Here is a structured project specification and development plan, formatted as a document you can use to guide your work and present to your AI coding assistant.


Build an AI Agent From Scratch in Python - Tutorial for Beginners - YouTube
Tech With Tim · 393K views

AI-PKMS-Project-Specification
Oct 16 at 9:04 PM

I have to create a project for a csc class using python language that revolves around the use of AI coding  assistants to plan, specify, develop, and test your own software that includes:
personal knowledge management system (PKMS)
personal task management system
a terminal-based chat interface to interact with your stored knowledge and tasks
AI agents that interact with the stored knowledge or tasks , and must run portably on Windows, OSX, Linux. The state should be stored in JSON documents, a SQLite database, or a Neo4J database. Think about ideas for what the project can be
That's a fantastic and challenging project assignment! I can definitely help you brainstorm some compelling project ideas that meet all your requirements, focusing on the seamless integration of PKMS, task management, and an AI agent in a terminal environment.

Here are three distinct project ideas—ranging from a professional focus to a more creative/academic focus—that fully satisfy the complexity and functionality requirements of your CSC class.

2. Project Idea: The Digital Architect's Journal (DevOps-Planner)
This idea focuses on a software developer's workflow, where the PKMS stores configuration details and technical solutions, and the task manager handles sprint or feature development.
Component,Focus & Functionality
PKMS (Knowledge),"Stores Code Snippets, Deployment Instructions (e.g., ""How to reset NGINX on Server B""), and Project Debug Logs. Tags include language, service, or bug_fix."
Task Management,"Tracks Feature Development (e.g., ""Implement user auth""), Bug Fixes, and Code Review items."
Terminal Interface,"User types in queries like: note add ""Python function for file upload"" --tags python, backend, or conversational queries."
AI Agent Core Skill,Troubleshooting and Planning.
AI Agent Tools,"1. search_logs(keyword): Finds relevant debug logs from past projects. 2. create_subtasks(parent_task_id, steps): Breaks down a large task into smaller, actionable sub-tasks in the database. 3. get_config_snippet(service_name): Retrieves the configuration from a past note."
Example AI Query,"""I'm facing a connection timeout error. What steps did I follow last time to fix the database connection issue, and can you generate a checklist task for me?"""
Data Storage,"JSON Documents (Ideal for storing semi-structured configuration snippets, with the file path stored in the Task/Note metadata)."

3. Project Idea: The Creative Content Hub (Writer-Assistant)
This idea is geared toward creative writing or content creation, where the PKMS holds ideas and character details, and tasks manage publication or chapter drafts.
Component,Focus & Functionality
PKMS (Knowledge),"Stores Character Profiles, World-Building Lore, Dialogue Snippets, and Plot Points. Tags include character_name, location, or theme."
Task Management,"Tracks Chapter Drafting, Idea Generation Sessions, and Editing Cycles. The due date system manages a personal publication schedule."
Terminal Interface,"User types in queries like: task complete 15, or conversational queries."
AI Agent Core Skill,Idea Generation and Content Retrieval.
AI Agent Tools,"1. get_character_profile(name): Retrieves a specific character's details. 2. suggest_plot_point(theme): Agent reads related notes and generates a new plot idea based on the stored lore, then saves it as a new note. 3. get_tasks_due_today(): Lists items needing immediate attention."
Example AI Query,"""What are the core themes associated with the character 'Evelyn,' and can you suggest a dark plot point related to that theme?"""
Data Storage,"Neo4J Database (A graph database is excellent for modeling relationships between Characters, Locations, and Plot Points, making the AI's retrieval logic more powerful)."


# PROMPT
I like the idea of number 1 (The Research Companion ) can you give me a study plan for this on concepts I should learn?

# Output(Gemini):
That is an excellent choice. The Research Companion (Academia-Agent) is a highly relevant project that showcases modern AI integration alongside solid computer science fundamentals like data persistence and structured architecture.

Since we've chosen the SQLite database for storage, this study plan will focus specifically on the concepts needed to successfully implement that design and its related AI tools.

Study Plan: The Research Companion (SQLite Focus)
This plan prioritizes the concepts most critical for implementation and grading, moving from fundamental persistence to advanced AI integration.

Phase 1: Data Modeling and Persistence (Days 1-2)

This phase is about mastering how to store and retrieve data reliably.

Concept Area	Focus	Key Deliverable & Practice
A. SQL & sqlite3	Schema Creation and Connection	Master the sqlite3 module in Python. Practice initializing the database file (.db) and ensuring the notes and tasks tables are created with the specified columns and constraints.
B. Data CRUD	Basic Database Functions	Write and test the four core SQL query types in Python functions: INSERT (Create), SELECT (Read), UPDATE (Update), and DELETE (Delete) for both the notes and tasks tables.
C. Parameterized Queries	Security and Integrity	Crucial: Learn to use ? placeholders in your SQL queries with the cursor.execute() method (e.g., cursor.execute("INSERT INTO notes VALUES (?, ?)", (content, tags))). This prevents SQL Injection and ensures data is handled correctly.
Phase 2: Application Architecture (Days 3-4)

This phase ensures your code is modular, testable, and maintainable, which is key for a good CSC grade.

Concept Area	Focus	Key Deliverable & Practice
A. Three-Layer Architecture	Separation of Concerns	Practice abstracting code into three distinct files (db_manager.py, service.py (containing PKMSService and TaskService), and cli.py). The Service Layer should contain functions like add_new_note() that call the database layer, but do not contain any SQL code themselves.
B. Python Classes & Dataclasses	Data Structuring	Learn to use Python's built-in dataclasses (or simple class definitions) to represent your data. Instead of passing around raw database tuples or dictionaries, your service layer functions should return instances of a Task object or a Note object.
C. Input/Output (I/O) Management	Portability	Master how to handle file paths reliably across different operating systems (os.path.join). The location of your pkms_data.db file should be determined portably.
Phase 3: AI Agent Integration (Days 5-7)

This is where you bridge your structured Python application with the LLM's reasoning engine.

Concept Area	Focus	Key Deliverable & Practice
A. LLM Tool-Calling	Agent-Tool Mechanism	Understand how to expose your Service Layer functions (e.g., add_task, get_notes_by_tag) to the LLM. This involves adding specific docstrings and type hints to your functions that the AI framework (like the Gemini API) can read.
B. System Prompt Engineering	Defining the Agent's Role	Practice writing a detailed and constrained System Prompt. The prompt must clearly instruct the LLM on: 1) Its persona (Research Companion), 2) When to use its tools, and 3) The required output format.
C. Conversation Management	Agent Memory	Learn how to maintain the history of the conversation, including the LLM's intermediate reasoning steps and the output from tool calls, and send that entire context back to the LLM in the next turn of the chat loop.
D. Structured Output	Reliable Data Exchange	For complex tasks (like "suggest a priority"), learn how to ask the LLM to return a predictable JSON object instead of free-form text. This makes it easy for your Python code to parse the AI's response and apply it to the database.
Recommended Libraries to Research

You should familiarize yourself with these libraries, as they will simplify the complex parts of the project:

sqlite3 (Standard Library): Your core persistence tool.

rich: Essential for creating the professional, colorful, and formatted terminal interface (TUI).

datetime (Standard Library): Needed for managing created_at and due_date fields in the database.

Gemini API SDK: The library you will use to connect your Python tools to the Large Language Model.

Let me know if you would like me to generate a simple example for Parameterized Queries in Python, as that is a foundational skill for this project!


# PROMPT
Make this into a 5 week schedule 


# Output(Gemini)
This is a great approach! Breaking down the project into a structured, 5-week schedule will ensure you meet all the requirements while maintaining a clean, well-engineered codebase.

This schedule is designed with an emphasis on early architectural setup (Weeks 1 & 2) and AI integration (Weeks 4 & 5), dedicating Week 3 to solidifying the core user experience.

5-Week Project Development Schedule: The Research Companion
📅 Week 1: Core Data Persistence and Modeling

Goal: Establish the unbreakable foundation of the database and the code structure.

Day	Focus Area	Tasks & Concepts	Key Deliverable
Mon	Project Setup & Architecture	Set up Python virtual environment (venv). Create initial project files (db_manager.py, pkms_service.py, task_service.py). Study: Three-Layer Architecture.	Project file structure initialized.
Tue	Database Schema	Write the SQL CREATE TABLE IF NOT EXISTS statements for the notes and tasks tables (with columns like title, status, content, tags). Study: SQLite Data Types.	Complete SQL schema definition.
Wed	DB Connection & Init	Implement the database connection and the initialize_db() function in db_manager.py. Study: sqlite3 Connection Management.	db_manager.py successfully creates the database file.
Thu	Task CRUD (Create/Read)	Write the add_task and get_all_tasks functions in task_service.py, using parameterized queries for security. Study: Parameterized Queries.	Task creation and listing functions working.
Fri	Task CRUD (Update/Delete)	Implement update_task_status and delete_task_by_id. Test all four task functions from a separate testing script. Study: UPDATE and DELETE SQL.	All core Task Management services are functional.
📅 Week 2: PKMS Services and Data Layer Refinement

Goal: Complete all core data services and prepare them for use by the interface and AI agent.

Day	Focus Area	Tasks & Concepts	Key Deliverable
Mon	Note CRUD (Create/Read)	Implement add_note and get_all_notes in pkms_service.py. Ensure tagging (comma-separated string) is handled correctly.	Core PKMS creation and retrieval is ready.
Tue	Note Search Logic	Implement search_notes_by_keyword using SQL LIKE and % wildcards for basic keyword search.	Functional note search service.
Wed	Data Structuring	Define Python dataclass models for Task and Note. Refactor all service layer functions to return lists of these objects, not raw database tuples. Study: Python dataclasses.	Service Layer outputs structured objects.
Thu	Error Handling & I/O	Add simple try...except blocks in the service layer to catch sqlite3 errors (e.g., database locked) and print informative messages.	Robust service layer with basic error handling.
Fri	Week 1 & 2 Review	Review all code for clean architecture compliance. Write and clean up all docstrings for every function in the Service Layer (this is crucial for the AI Agent in Week 4).	Codebase clean and ready for CLI development.
📅 Week 3: Terminal Interface (TUI) Development

Goal: Build the basic text-based user interface and integrate it with the completed service layer.

Day	Focus Area	Tasks & Concepts	Key Deliverable
Mon	CLI Setup & rich Integration	Install rich. Create cli.py and set up the main command loop. Study: rich tables and panels.	Basic text input loop running.
Tue	Task Listing Display	Use rich to display the list of tasks in a clean, colored table, sorted by priority and due date. Implement visual differentiation (e.g., red for high priority).	Aesthetic, readable task list TUI.
Wed	PKMS Display & Filtering	Implement a command to display a note by ID and another command to list notes, using rich panels for clear presentation.	Functional and readable PKMS viewing in the terminal.
Thu	Command Parsing	Implement the core input logic in cli.py: checking if user input is a direct command (e.g., task done 5) or a generic query (which gets passed to the future AI agent).	User input is correctly categorized.
Fri	CLI Testing	Manually test every user command (add, view, update, delete, search) to ensure it works correctly and the terminal feedback is clear.	Fully functional non-AI command-line application.
📅 Week 4: AI Agent Tool-Calling and Reasoning

Goal: Integrate the LLM, define the tools, and establish the AI's core reasoning loop.

Day	Focus Area	Tasks & Concepts	Key Deliverable
Mon	LLM Setup & Tools Definition	Install the Gemini SDK. Define a System Prompt for the "Research Companion." Create the AI Tool wrappers in ai_tools.py using functions from your service.py. Study: AI Tool/Function Calling.	Basic LLM connection and tool registry established.
Tue	Core Tool: Task Creation	Implement the logic to allow the AI to call the add_task function. Test by prompting: "Please add a task to review chapter 5 by tomorrow."	AI successfully calls the add_task tool.
Wed	Core Tool: Knowledge Retrieval	Implement the logic for the AI to call search_notes_by_keyword. Test by prompting: "What did I write about database transactions?"	AI successfully retrieves and reasons over notes.
Thu	AI Logic: Intent Routing	Refine the main chat loop to send the full conversation history (Memory) and the tool definitions to the LLM. The LLM must decide whether to respond directly or call a tool. Study: Conversation History & Context.	Chat interface can successfully route queries to tools or direct response.
Fri	AI Logic: Summarization	Test the AI's ability to use the retrieved text from its tool call and formulate a concise, human-readable summary for the user.	AI Agent successfully synthesizes information.
📅 Week 5: Finalization, Testing, and Documentation

Goal: Finalize complex agent features, write comprehensive unit tests, and prepare final project documentation.

Day	Focus Area	Tasks & Concepts	Key Deliverable
Mon	Advanced Agent Tool (Prioritization)	Implement an advanced AI function (e.g., an LLM call asking it to "suggest a priority level" based on the task title/due date and return a structured JSON update).	Advanced agent functionality complete.
Tue	Unit Testing (Services)	Write unit tests for your db_manager.py and all functions in your pkms_service.py and task_service.py. Focus on testing the data logic, not the AI calls. Study: Python unittest or pytest.	All core application logic is unit-tested.
Wed	Integration Testing (AI Tools)	Design specific test cases to prove the AI correctly calls all three primary tools (add_task, search_notes, and the advanced prioritization tool).	AI integration verified across all core functions.
Thu	Final Polish & Portability Check	Finalize requirements.txt. Add comprehensive comments and docstrings. Write a short README explaining how to run the project using the virtual environment.	Project fully documented and ready for deployment.
Fri	Project Submission	Final review, bug fixes, and preparation for submission.	Project Submitted!

# Prompt User:
Now could I please get a prototype that can be used for visual studio code without any comments 

# Output( Gemini):
import sqlite3
import json
import requests
import time
from datetime import datetime
from typing import List, Dict, Any, Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown

API_KEY = ""
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"
DB_NAME = "pkms_data.db"
console = Console()

class DBManager:
    """Handles connection and initialization of the SQLite database."""
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.conn = None
        self.initialize_db()

    def connect(self):
        if self.conn is None:
            try:
                self.conn = sqlite3.connect(self.db_name)
                self.conn.row_factory = sqlite3.Row
            except sqlite3.Error as e:
                console.print(f"[bold red]Database Connection Error:[/bold red] {e}")
                raise

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def initialize_db(self):
        self.connect()
        try:
            cursor = self.conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    tags TEXT,
                    created_at TEXT NOT NULL,
                    source TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    due_date TEXT,
                    priority INTEGER
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            console.print(f"[bold red]Database Initialization Error:[/bold red] {e}")
        finally:
            self.close()

class ResearchCompanionService:
    """Contains all core business logic and database interactions."""

    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def add_task(self, title: str, due_date: str = None, priority: int = 3) -> int:
        """Adds a new task. Returns the new task's ID."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO tasks (title, status, due_date, priority) VALUES (?, 'TODO', ?, ?)",
                           (title, due_date, priority))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            console.print(f"[bold red]Error adding task:[/bold red] {e}")
            return -1
        finally:
            conn.close()

    def update_task_status(self, task_id: int, new_status: str) -> bool:
        """Updates the status of a specific task."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            console.print(f"[bold red]Error updating task:[/bold red] {e}")
            return False
        finally:
            conn.close()

    def list_tasks(self, status: str = 'TODO', order_by: str = 'priority') -> List[Dict[str, Any]]:
        """Lists tasks, filtered by status and sorted."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            query = f"SELECT id, title, status, due_date, priority FROM tasks WHERE status = ? ORDER BY {order_by} ASC"
            cursor.execute(query, (status,))
            return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            console.print(f"[bold red]Error listing tasks:[/bold red] {e}")
            return []
        finally:
            conn.close()

    def add_note(self, content: str, tags: str = None, source: str = None) -> int:
        """Adds a new research note. Returns the new note's ID."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        created_at = datetime.now().isoformat()
        try:
            cursor.execute("INSERT INTO notes (content, tags, created_at, source) VALUES (?, ?, ?, ?)",
                           (content, tags, created_at, source))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            console.print(f"[bold red]Error adding note:[/bold red] {e}")
            return -1
        finally:
            conn.close()

    def search_notes(self, keyword: str) -> List[Dict[str, Any]]:
        """Performs a basic keyword search across note content and tags."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            search_term = f'%{keyword.lower()}%'
            cursor.execute("""
                SELECT id, SUBSTR(content, 1, 100) AS snippet, tags, source 
                FROM notes 
                WHERE LOWER(content) LIKE ? OR LOWER(tags) LIKE ?
            """, (search_term, search_term))
            return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            console.print(f"[bold red]Error searching notes:[/bold red] {e}")
            return []
        finally:
            conn.close()

service = ResearchCompanionService()

def add_task_tool(title: str, due_date: Optional[str] = None, priority: int = 3) -> str:
    """
    Creates a new task in the task management system.
    Args:
        title (str): The concise title of the task to be created.
        due_date (Optional[str]): The target date for task completion (YYYY-MM-DD). Default is None.
        priority (int): The importance level, where 1 is highest priority and 5 is lowest. Default is 3.
    Returns:
        str: A confirmation message indicating the task ID.
    """
    task_id = service.add_task(title, due_date, priority)
    if task_id > 0:
        return f"Successfully created a new task with ID {task_id}: '{title}'."
    else:
        return "Failed to create task due to a database error."

def get_research_notes_tool(keyword: str) -> str:
    """
    Searches the PKMS for relevant notes based on a keyword query.
    Args:
        keyword (str): The main topic or concept to search for (e.g., 'Deep Learning' or 'SQLite').
    Returns:
        str: A JSON string of the search results, including note ID, snippet, and tags.
    """
    notes = service.search_notes(keyword)
    if not notes:
        return "No relevant notes found for that keyword."

    results = [{"id": n['id'], "snippet": n['snippet'] + "...", "tags": n['tags']} for n in notes]
    return json.dumps(results)

def list_tasks_tool(status: str = 'TODO') -> str:
    """
    Lists all tasks currently in a specified status (default is 'TODO').
    Args:
        status (str): The status of tasks to list (e.g., 'TODO', 'IN_PROGRESS', 'DONE'). Default is 'TODO'.
    Returns:
        str: A JSON string containing the IDs, titles, due dates, and priorities of the tasks.
    """
    tasks = service.list_tasks(status=status)
    if not tasks:
        return f"No tasks found with status '{status}'."

    results = [{"id": t['id'], "title": t['title'], "priority": t['priority'], "due_date": t['due_date']} for t in tasks]
    return json.dumps(results)

TOOL_FUNCTIONS = {
    "add_task_tool": add_task_tool,
    "get_research_notes_tool": get_research_notes_tool,
    "list_tasks_tool": list_tasks_tool,
}

TOOLS_DEFINITION = [
    {
        "function_declarations": [
            {
                "name": name,
                "description": func.__doc__.strip(),
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        p: {"type": t.__name__.upper()}
                        for p, t in func.__annotations__.items()
                        if p not in ('return', 'title')
                    }
                }
            }
            for name, func in TOOL_FUNCTIONS.items()
        ]
    }
]

def call_gemini_agent(prompt: str, chat_history: List[Dict[str, Any]]):
    """
    Communicates with the Gemini API, handles tool calling, and manages history.
    """
    if not API_KEY:
        console.print(Panel(
            "[bold yellow]⚠️ Gemini API Key Missing ⚠️[/bold yellow]\n"
            "AI Agent functionality is disabled. Please provide an API Key.\n"
            "This prototype will only return the tool-calling structure.",
            title="[bold red]Agent Status[/bold red]"
        ))
        if "task" in prompt.lower():
             return [{"role": "model", "parts": [
                {"function_call": {"name": "add_task_tool", "args": {"title": prompt, "due_date": str(datetime.now().date())}}}
            ]}]
        return [{"role": "model", "parts": [{"text": "Hello! I am the Research Companion. Since the API key is missing, I am unable to process your request conversationally, but the tool-calling structure is ready."}]}]


    system_instruction = (
        "You are the Research Companion, a sophisticated AI agent dedicated to managing "
        "a user's Personal Knowledge Management System (PKMS) and Task List. "
        "Your primary goal is to assist the user with academic planning and research synthesis. "
        "Use the provided tools whenever a user request involves creating, modifying, or retrieving tasks or notes. "
        "If a user asks a general question, answer it conversationally. If a user asks to summarize notes, "
        "you MUST call 'get_research_notes_tool' first, then use the result to synthesize the final answer."
    )

    contents = [
        {"role": "user", "parts": [{"text": prompt}]}
    ]

    payload = {
        "systemInstruction": {"parts": [{"text": system_instruction}]},
        "contents": contents,
        "tools": [{"function_declarations": [
            d for item in TOOLS_DEFINITION for d in item['function_declarations']
        ]}],
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(
                API_URL,
                headers={'Content-Type': 'application/json'},
                json=payload,
                params={'key': API_KEY}
            )
            response.raise_for_status()
            
            result = response.json()
            return result.get('candidates', [])

        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]API Error (Attempt {attempt + 1}/{max_retries}):[/bold red] {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return [{"role": "model", "parts": [{"text": "AI Agent failed to connect after multiple retries. Please check the API key and network connection."}]}]
    return []

def execute_tool_call(function_call: Dict[str, Any]) -> Dict[str, Any]:
    """Executes the Python function requested by the LLM."""
    name = function_call['name']
    args = function_call.get('args', {})

    tool_func = TOOL_FUNCTIONS.get(name)
    if not tool_func:
        return {"function_response": {"name": name, "response": f"Tool '{name}' not found."}}

    console.print(f"[bold blue]🤖 Calling Tool:[/bold blue] {name}({json.dumps(args)})")
    
    result = tool_func(**args)
    
    return {
        "function_response": {
            "name": name,
            "response": {"content": result}
        }
    }

def display_tasks(tasks: List[Dict[str, Any]]):
    """Displays a list of tasks using the rich library."""
    if not tasks:
        console.print(Panel("[bold yellow]No tasks found.[/bold yellow]"))
        return

    table = Table(title="[bold green]Active Tasks[/bold green]", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Priority", justify="center")
    table.add_column("Title", style="cyan", min_width=40)
    table.add_column("Status", justify="center")
    table.add_column("Due Date")

    for task in tasks:
        priority_style = {1: "bold red", 2: "yellow", 3: "green", 4: "dim white", 5: "dim white"}.get(task['priority'], "white")
        table.add_row(
            str(task['id']),
            f"[{priority_style}]{task['priority']}[/{priority_style}]",
            task['title'],
            f"[bold blue]{task['status']}[/bold blue]",
            task['due_date'] if task['due_date'] else "N/A"
        )
    console.print(table)

def main_loop():
    """Main application entry point and chat loop."""
    db_manager = DBManager()
    chat_history = []
    
    console.print(Panel(
        "[bold green]Welcome to the Research Companion (Academia-Agent)[/bold green]\n"
        "Type 'help' for commands, or start a conversational query for the AI.\n"
        "Database is ready at: [italic]{}[/italic]".format(DB_NAME),
        title="[bold blue]PKMS CLI[/bold blue]"
    ))

    service.add_note("The ReAct pattern in AI agents involves a loop of Reason, Act, and Observe.", "AI Agents, ReAct", "GPT-3 research")
    service.add_task("Finalize CSC Project Report Draft", "2025-10-24", 1)

    while True:
        try:
            prompt = console.input("[bold yellow]You > [/bold yellow]").strip()

            if prompt.lower() in ('quit', 'exit'):
                console.print("[bold green]Research Companion shutting down. Goodbye![/bold green]")
                break
            elif prompt.lower() == 'help':
                console.print(Markdown("""
**Available Commands (CLI)**:
* `list tasks`: Display all pending tasks.
* `list notes <keyword>`: Search notes by keyword.
* `help`: Show this message.
* `quit`/`exit`: Close the application.
"""))
                continue
            elif prompt.lower() == 'list tasks':
                tasks = service.list_tasks(status='TODO')
                display_tasks(tasks)
                continue
            elif prompt.lower().startswith('list notes'):
                keyword = prompt[11:].strip()
                notes = service.search_notes(keyword if keyword else "")
                
                if notes:
                    notes_table = Table(title=f"[bold cyan]Search Results for '{keyword}'[/bold cyan]", show_header=True, header_style="bold blue")
                    notes_table.add_column("ID", style="dim", width=4)
                    notes_table.add_column("Snippet (First 100 chars)", style="white")
                    notes_table.add_column("Tags", style="green")
                    for n in notes:
                         notes_table.add_row(str(n['id']), n['snippet'], n['tags'] if n['tags'] else "N/A")
                    console.print(notes_table)
                else:
                    console.print("[yellow]No matching notes found.[/yellow]")
                continue
            
            candidates = call_gemini_agent(prompt, chat_history)
            
            if not candidates:
                console.print("[bold red]Error: No response from AI Agent.[/bold red]")
                continue
            
            candidate = candidates[0]
            
            if 'text' in candidate['content']['parts'][0]:
                response_text = candidate['content']['parts'][0]['text']
                console.print(Panel(Markdown(response_text), title="[bold magenta]AI Response[/bold magenta]"))
                continue

            while 'function_call' in candidate['content']['parts'][0]:
                function_call = candidate['content']['parts'][0]['function_call']
                tool_output = execute_tool_call(function_call)
                
                tool_call_history = [
                     {"role": "user", "parts": [{"text": prompt}]},
                     {"role": "model", "parts": [
                         {"function_call": function_call}
                     ]},
                     {"role": "function", "parts": [
                         {"function_response": tool_output["function_response"]}
                     ]}
                ]

                console.print("[bold green]🤖 Thinking... (Processing tool results)[/bold green]")
                second_call_payload = {
                    "contents": tool_call_history,
                    "tools": TOOLS_DEFINITION,
                }
                
                second_call_response = requests.post(
                    API_URL,
                    headers={'Content-Type': 'application/json'},
                    json=second_call_payload,
                    params={'key': API_KEY}
                )

                second_result = second_call_response.json()
                second_candidate = second_result.get('candidates', [{}])[0]
                
                if 'text' in second_candidate['content']['parts'][0]:
                    final_response_text = second_candidate['content']['parts'][0]['text']
                    console.print(Panel(Markdown(final_response_text), title="[bold magenta]AI Response[/bold magenta]"))
                    break
                else:
                    candidate = second_candidate
            
        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")
  if __name__ == "__main__":
    main_loop()
