import json
from datetime import datetime

def get_lessons(teacher_id=None, student_id=None, date=None):
    """Get lessons with optional filtering by teacher, student, or date"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            lessons = data.get('lessons', [])

        # Apply filters
        if teacher_id:
            lessons = [l for l in lessons if l['teacher_id'] == teacher_id]
        if student_id:
            lessons = [l for l in lessons if l['student_id'] == student_id]
        if date:
            lessons = [l for l in lessons if l['date'].startswith(date)]  # date format: "YYYY-MM-DD"

        return True, lessons
    except FileNotFoundError:
        return False, "No lessons found"
    except Exception as e:
        return False, f"Error retrieving lessons: {str(e)}"

def add_lesson(lesson_data):
    """Add a new lesson to the schedule"""
    try:
        if not all(key in lesson_data for key in ['teacher_id', 'student_id', 'date', 'time', 'duration']):
            return False, "Missing required lesson data"

        with open('data.json', 'r') as f:
            data = json.load(f)

        # Create new lesson
        new_lesson = {
            'id': len(data.get('lessons', [])) + 1,
            'teacher_id': lesson_data['teacher_id'],
            'student_id': lesson_data['student_id'],
            'date': lesson_data['date'],
            'time': lesson_data['time'],
            'duration': lesson_data['duration'],
            'status': 'scheduled'
        }

        # Add to lessons list
        if 'lessons' not in data:
            data['lessons'] = []
        data['lessons'].append(new_lesson)

        # Save updated data
        with open('data.json', 'w') as f:
            json.dump(data, f)

        return True, "Lesson scheduled successfully"
    except Exception as e:
        return False, f"Error scheduling lesson: {str(e)}"

def update_lesson_status(lesson_id, new_status):
    """Update the status of a lesson (e.g., 'completed', 'cancelled')"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Find and update lesson
        for lesson in data.get('lessons', []):
            if lesson['id'] == lesson_id:
                lesson['status'] = new_status
                
                # Save updated data
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                    
                return True, f"Lesson status updated to {new_status}"
                
        return False, "Lesson not found"
    except Exception as e:
        return False, f"Error updating lesson status: {str(e)}"

def mark_attendance(lesson_id):
    """Mark attendance for a lesson by updating its status"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Find and update lesson status to 'completed'
        for lesson in data.get('lessons', []):
            if lesson['id'] == lesson_id:
                lesson['status'] = 'completed'
                
                # Save updated data
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                return True, "Attendance marked successfully."

        return False, "Lesson not found."
    except Exception as e:
        return False, f"Error marking attendance: {str(e)}"

def display_lessons():
    # Logic to fetch and display lessons
    try:
        with open('lessons.json', 'r') as f:
            lessons = json.load(f)
            return lessons  # Return the list of lessons
    except FileNotFoundError:
        print("No lessons found.")
        return []
