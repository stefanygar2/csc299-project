This prototype is a conversational front-end designed to query the knowledge and task data created by the Core PKMS. It provides an interactive way to retrieve information using natural language keywords.


# 🚀 Setup & Execution

Ensure Python is installed: (Python 3.6+ recommended)

Run the script:

python pkm_chat.py


# 🤖 Interaction & Querying

The application starts an endless loop, allowing you to type questions:

 
Task Search

What tasks are due soon?

Searches the tasks.json file. Defaults to showing pending tasks.

Task Search

Show completed tasks related to "project X"

Filters completed tasks based on keywords in the title or description.

Knowledge Search

find information about "machine learning"

Searches knowledge.json entries for keywords in the title, content, and tags.

Knowledge Search

notes on "quantum physics" and tags

Searches for knowledge based on a combination of keywords.

Exit

exit or quit

Closes the chat interface.

Note: The chat uses simple keyword matching and regular expressions to find results, acting as a basic search engine over your JSON data.
