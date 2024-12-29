import json
from datetime import datetime
import re

def load_list(filename='StoreList.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_list(list, filename='StoreList.json'):
    with open(filename, 'r') as file:
        json.dump(list, file, indent=4)

def extract_tags(content):
    words = re.findall(r'\b\w{4,}\b', content)
    return list(set(words))

# ADDING NOTES
# Add Task:
# Input: Task title and optional description.
# Output: Task is added to the list and saved to the JSON file.
# View Tasks:

# Input: Request to view all tasks.
# Output: Display a list of all tasks with their titles and descriptions.

# Update Task:
# Input: Task index, new title (optional), and new description (optional).
# Output: The specified task is updated with the new information and saved to the JSON file.

# Delete Task:
# Input: Task index.
# Output: The specified task is removed from the list and the JSON file is updated.

# Search Tasks:
# Input: Keyword or regex pattern.
# Output: Display a list of tasks that match the search criteria.

# Additional Requirements:
# The application should be implemented in Python.
# Use the json module for storing tasks in a JSON file.
# Use the re module for searching tasks using regular expressions.

# Expected Outputs:

# For Adding a Task: Confirmation that the task has been added.
# For Viewing Tasks: A list of all tasks with their details.
# For Updating a Task: Confirmation that the task has been updated.
# For Deleting a Task: Confirmation that the task has been deleted.
# For Searching Tasks: A filtered list of tasks that match the search criteria.
