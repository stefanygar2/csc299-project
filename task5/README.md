# Task 5 
A student planner built using a Personal Knowledge Management System (PKMS) approach. It was developed following the structured Spec Kit methodology, ensuring all implementation strictly adheres to the initial project specifications. The application manages assignments, tracks a students status, handles rich-text notes (Markdown), and implements interlinking between tasks (a core PKMS feature).

# 🛠️ Setup and Installation
Prerequisites
Python 3.8+
The pip package installer
# 1. Activate Virtual Enviroment 
source /path/to/your/venv/bin/activate

2. install 
(venv) $ pip install pytest pytest-mock
Run the task manager CLI: py -m src.tasks_manager
''' 
task5/
├── src/
│   └── tasks_manager.py       
├── data/
│   ├── nodes.json             
│   ├── tasks.json             
│   └── links.json           
├── tests/
│   └── test_tasks_manager.py 
├── specify/
│   ├── memory/
│   │   └── constitution.md    <- Project rules
│   ├── scripts/bash/
│   │   └── run_tests.sh       <- Example script
│   └── templates/
│       └── plan-template.md   <- Spec Kit template
├── .gitignore
├── pyproject.toml
└── README.md
'''
