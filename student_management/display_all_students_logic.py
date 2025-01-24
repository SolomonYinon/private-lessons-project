import json

def display_all_students():
    # Logic to display all students
    try:
        with open('students.json', 'r') as f:
            students = json.load(f)
            return students  # Return the list of students
    except FileNotFoundError:
        print("No students found.")
        return []
