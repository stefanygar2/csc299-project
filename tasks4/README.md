this is a standalone experiment to try out the OpenAI Chat Completions API, so you do not need to copy over any of your PKMS/task software
use the OpenAI Chat Completions API to send a paragraph-length description of a task to ChatGPT-5-mini and have it summarize the task as a short phrase
add a loop to your code so that it can summarize multiple paragraph-length descriptions (independently of one another)
add at least 2 sample paragraph-length descriptions to your code so that running uv run tasks4 will summarize both descriptions and then print the summaries

# HOW TO RUN 
cd tasks4
uv run python __main__.py
