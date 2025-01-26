import json

def validate_data(name, email):
    if not name or not email:
        return False
    if '@' not in email:
        return False
    return True


def user_exists(email):
    try:
        with open('data.json', 'r') as f:
            users = f.readlines()
            for user in users:
                if json.loads(user)['email'] == email:
                    return True
    except FileNotFoundError:
        return False
    return False

def validate_registration_data(student_data):
    # Basic validation
    if not all([student_data.get('name'), student_data.get('email'), student_data.get('grade')]):
        return False, "All fields are required"
    
    if '@' not in student_data['email']:
        return False, "Invalid email format"
    
    return True, "Validation successful"

def save_registration(student_data):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            
            # Check if email already exists
            if any(s['email'] == student_data['email'] for s in data.get('students', [])):
                return False, "Email already registered"
            
            # Create new student record
            new_student = {
                'id': len(data.get('students', [])) + 1,
                'name': student_data['name'],
                'email': student_data['email'],
                'grade': student_data['grade'],
                'active': True,
                'registered': True,
                'paid': False
            }
            
            # Add to students list
            if 'students' not in data:
                data['students'] = []
            data['students'].append(new_student)
            
            # Save updated data
            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            return True, "Registration successful"
            
    except FileNotFoundError:
        # Create new data file with first student
        data = {
            'students': [{
                'id': 1,
                'name': student_data['name'],
                'email': student_data['email'],
                'grade': student_data['grade'],
                'active': True,
                'registered': True,
                'paid': False
            }]
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)
        return True, "Registration successful"
    except Exception as e:
        return False, f"Error during registration: {str(e)}"
