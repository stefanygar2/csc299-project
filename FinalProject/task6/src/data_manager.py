import json
import os
from typing import List, Type, TypeVar, Dict, Any

# Define a generic type for our standard model classes
T = TypeVar('T')

class DataManager:
    """Handles loading and saving model objects to JSON files."""

    def __init__(self, data_dir: str = ".data"):
        # Create data directory if it doesn't exist (portable)
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.pkm_path = os.path.join(self.data_dir, "knowledge.json")
        self.task_path = os.path.join(self.data_dir, "tasks.json")

    def _load_file(self, filepath: str) -> List[Dict[str, Any]]:
        """Reads and parses a JSON file."""
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from {filepath}. Starting with empty list.")
            return []

    def _save_file(self, filepath: str, data: List[Dict[str, Any]]):
        """Writes a list of dictionaries to a JSON file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def load_data(self, model_class: Type[T], file_type: str) -> List[T]:
        """Loads data from a specified file path and converts to model objects."""
        filepath = self.pkm_path if file_type == 'pkm' else self.task_path
        raw_data = self._load_file(filepath)
        # Use the class method 'from_dict' for deserialization
        return [model_class.from_dict(d) for d in raw_data]

    def save_data(self, data: List[Any], file_type: str):
        """Saves a list of model objects to a specified file path."""
        filepath = self.pkm_path if file_type == 'pkm' else self.task_path
        # Use the instance method 'to_dict' for serialization
        raw_data = [d.to_dict() for d in data]
        self._save_file(filepath, raw_data)
        print(f"\n--- Data saved successfully to {filepath} ---")
