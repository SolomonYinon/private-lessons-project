import json

def display_lessons():
    # Logic to fetch and display lessons
    try:
        with open('lessons.json', 'r') as f:
            lessons = json.load(f)
            return lessons  # Return the list of lessons
    except FileNotFoundError:
        print("No lessons found.")
        return []
