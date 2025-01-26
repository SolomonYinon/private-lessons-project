import json

def display_students():
    # Logic to fetch and display students for the teacher
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            
            # Get all lessons for the teacher
            teacher_lessons = [
                lesson for lesson in data.get('lessons', [])
            ]
            
            # Get all student IDs from these lessons
            student_ids = set()
            for lesson in teacher_lessons:
                student_ids.update(lesson.get('student_ids', []))
            
            # Get student details
            students = []
            for student in data.get('students', []):
                if str(student['id']) in student_ids:
                    students.append({
                        'id': student['id'],
                        'name': student['name'],
                        'email': student.get('email', 'N/A'),
                        'grade': student.get('grade', 'N/A'),
                        'status': 'Active' if student.get('active', True) else 'Inactive'
                    })
            
            return students  # Return the list of students
    except FileNotFoundError:
        print("No students found.")
        return []

def get_teacher_students(teacher_id=None):
    """Get all students for a specific teacher or all students if no teacher ID is provided"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            if teacher_id:
                students = []
                for lesson in data.get('lessons', []):
                    if lesson['teacher_id'] == teacher_id:
                        for student_id in lesson.get('student_ids', []):
                            student = next((s for s in data.get('students', []) if s['id'] == student_id), None)
                            if student:
                                students.append(student)
                return students
            else:
                return data.get('students', [])  # Return all students
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error retrieving students: {str(e)}")
        return []

def get_student_details(student_id):
    """Get details for a specific student"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            return next((s for s in data.get('students', []) if s['id'] == student_id), None)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error retrieving student details: {str(e)}")
        return None
