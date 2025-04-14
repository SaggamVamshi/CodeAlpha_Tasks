import json

def load_data(file_path):
    """Load training data from a specified file path."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_conversation(conversation, file_path):
    """Save conversation to a specified file path."""
    with open(file_path, 'a') as file:
        for line in conversation:
            file.write(line + '\n')
