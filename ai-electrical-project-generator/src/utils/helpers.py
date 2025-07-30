# This file contains utility functions that can be used throughout the application.

def log_message(message: str) -> None:
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def save_to_file(data: dict, filename: str) -> None:
    """Saves the given data to a file in JSON format."""
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)