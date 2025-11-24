import os
from typing import List
from .models import Task, KnowledgeEntry

# Check for API key (though we use a mock, this is good practice)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

class LLMAgent:
    """Handles interaction with a Language Model for PKMS tasks."""

    def __init__(self):
        # In a real app, initialize the OpenAI client here
        if not OPENAI_API_KEY:
            print("--- WARNING: OPENAI_API_KEY not found. Using Mock LLM. ---")
        # self.client = OpenAI() # Real initialization

    def _mock_llm_call(self, prompt: str, task: str) -> str:
        """Mocks the LLM API call for portability."""
        if task == "summarize":
            # Deterministic summary based on content length
            return f"AI Summary: A concise overview of the document, focusing on {prompt.split()[0]} and covering {len(prompt.split())} unique tokens."
        elif task == "prioritize":
            # Simple logic based on keywords
            if any(word in prompt.lower() for word in ["critical", "deadline", "urgent"]):
                return "high"
            elif len(prompt) > 200:
                return "medium"
            return "low"
        return "mock_error"

    def summarize_entry(self, entry: KnowledgeEntry) -> str:
        """Generates a summary for a knowledge entry using the LLM."""
        
        prompt = f"Please provide a 50-word summary of the following knowledge entry:\nTitle: {entry.title}\nContent: {entry.content}"
        
        # --- Real OpenAI API Call (Requires API Key) ---
        # if OPENAI_API_KEY:
        #     try:
        #         response = self.client.chat.completions.create(
        #             model="gpt-4o-mini",
        #             messages=[
        #                 {"role": "system", "content": "You are a helpful knowledge summarization agent."},
        #                 {"role": "user", "content": prompt}
        #             ]
        #         )
        #         return response.choices[0].message.content.strip()
        #     except Exception as e:
        #         print(f"OpenAI Error during summarization: {e}")
        #         return f"Error: Could not summarize (LLM failure)."
        
        # --- Mock LLM Call (Default) ---
        return self._mock_llm_call(prompt, task="summarize")


    def prioritize_task(self, task: Task, linked_content: str) -> str:
        """Determines task priority (low/medium/high) using the LLM."""

        prompt = (
            f"Analyze the following task and context to assign a priority level (low, medium, or high). "
            f"Only return the priority level string itself.\n"
            f"Task: {task.title} (Due: {task.due_date})\n"
            f"Description: {task.description}\n"
            f"Linked Context: {linked_content}"
        )
        
        # --- Real OpenAI API Call (Requires API Key) ---
        # if OPENAI_API_KEY:
        #     try:
        #         # Using structured output for reliability
        #         response = self.client.chat.completions.create(
        #             model="gpt-4o-mini",
        #             messages=[
        #                 {"role": "system", "content": "You are a task prioritization agent. Respond ONLY with 'low', 'medium', or 'high'."},
        #                 {"role": "user", "content": prompt}
        #             ]
        #         )
        #         return response.choices[0].message.content.strip().lower()
        #     except Exception as e:
        #         print(f"OpenAI Error during prioritization: {e}")
        #         return "medium" # Default fallback
        
        # --- Mock LLM Call (Default) ---
        return self._mock_llm_call(prompt, task="prioritize")
