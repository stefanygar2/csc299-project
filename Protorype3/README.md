 Prototype 3: AI Agent Integration (pkm_agent.py)

This prototype demonstrates how an AI Agent can automatically interact with your PKMS data to perform valuable background processing, specifically Knowledge Summarization and Task Prioritization.

# ⚠️ Prerequisites

Core Data: You must have knowledge.json and tasks.json files populated from running pkm_core.py.

AI Service: In a real-world scenario, this script would require API keys and external library installations (requests, openai, etc.) to connect to a cloud LLM service. This prototype uses a Mock LLM Function for portability.

# 🚀 Setup & Execution

Ensure Python is installed: (Python 3.6+ recommended)

Run the agent cycle:

python pkm_agent.py

# ⚙️ Agent Functions

The agent runs a single, complete processing cycle when executed.

1. Summarization

Target: KnowledgeEntry objects in knowledge.json that do not currently have a value in the summary field (i.e., is_summarized is false).

Action: The agent sends the entry's full title and content to the (mocked) LLM.

Result: A generated summary is saved back to the summary field, and the entry is marked as processed.

2. Task Prioritization

Target: Task objects in tasks.json that are "pending" and have not yet been processed by the agent (i.e., is_prioritized is false).

Action: The agent analyzes the task's description and any linked knowledge content. It sends this context to the (mocked) LLM to determine a priority level (low, medium, or high).

Result: The new priority is saved to the task's priority field, and the task is marked as processed.

# 💾 Saving

After both processes run, the agent checks if any changes were made and updates the knowledge.json and tasks.json files with the new summaries and priorities.

To trigger the agent to re-process an entry or task, you would manually edit the JSON file and remove the summary value or reset the priority to "medium".
