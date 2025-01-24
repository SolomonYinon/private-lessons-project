import json

def display_students():
    # Logic to fetch and display students for the teacher
    try:
        with open('students.json', 'r') as f:
            students = json.load(f)
            return students  # Return the list of students
    except FileNotFoundError:
        print("No students found.")
        return []
