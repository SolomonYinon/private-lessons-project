import json

def get_all_students():
    """Get all students from the data file"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            students = [{
                'id': student['id'],
                'name': student['name'],
                'email': student.get('email', 'N/A'),
                'grade': student.get('grade', 'N/A'),
                'status': 'Active' if student.get('active', True) else 'Inactive'
            } for student in data.get('students', [])]
            return True, students
    except FileNotFoundError:
        return False, "No students found."
    except Exception as e:
        return False, f"Error retrieving students: {str(e)}"

def update_student(student_id, updated_data):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Find and update the student
        for student in data.get('students', []):
            if student['id'] == student_id:
                student.update(updated_data)
                break
        
        # Save the updated data
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return True, "Student updated successfully"
    except FileNotFoundError:
        return False, "Data file not found"
    except Exception as e:
        return False, f"Error updating student: {str(e)}"

def delete_student(student_id):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Find and remove the student
        data['students'] = [s for s in data['students'] if s['id'] != student_id]
        
        # Save the updated data
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return True, "Student deleted successfully"
    except FileNotFoundError:
        return False, "Data file not found"
    except Exception as e:
        return False, f"Error deleting student: {str(e)}"
