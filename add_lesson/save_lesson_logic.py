import json
from datetime import datetime

def get_teachers():
    """Get all active teachers from the data file"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            teachers = [t for t in data.get('teachers', []) if t.get('active', True)]
            return True, teachers
    except FileNotFoundError:
        return False, "Data file not found"
    except Exception as e:
        return False, f"Error retrieving teachers: {str(e)}"

def save_lesson(lesson_data):
    """Save a new lesson to the data file"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'lessons': []}
    except Exception as e:
        return False, f"Error reading data file: {str(e)}"
    
    try:
        # Parse and validate the schedule
        schedule_dt = datetime.strptime(lesson_data['schedule'], "%Y-%m-%d %H:%M")
        
        # Create the new lesson
        new_lesson = {
            'id': len(data.get('lessons', [])) + 1,
            'name': lesson_data['subject'],
            'teacher_id': int(lesson_data['teacher_id']),
            'student_id': int(lesson_data['student_id']),
            'date': schedule_dt.strftime("%Y-%m-%d"),
            'time': schedule_dt.strftime("%H:%M"),
            'duration': 60,
            'status': 'scheduled'
        }
        
        # Initialize lessons list if it doesn't exist
        if 'lessons' not in data:
            data['lessons'] = []
        
        # Add the new lesson
        data['lessons'].append(new_lesson)
        
        # Save the updated data
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return True, "Lesson scheduled successfully"
    
    except ValueError as e:
        return False, f"Invalid data format: {str(e)}"
    except Exception as e:
        return False, f"Error saving lesson: {str(e)}"
