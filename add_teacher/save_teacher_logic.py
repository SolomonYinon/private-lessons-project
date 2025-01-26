import json

def validate_teacher_email(email, data):
    return not any(teacher['email'] == email for teacher in data.get('teachers', []))

def save_teacher(teacher_data):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'teachers': []}

    if not validate_teacher_email(teacher_data['email'], data):
        return False, "Email already registered"

    new_teacher = {
        'id': len(data.get('teachers', [])) + 1,
        'name': teacher_data['name'],
        'email': teacher_data['email'],
        'subject': teacher_data['subject']
    }

    if 'teachers' not in data:
        data['teachers'] = []
    
    data['teachers'].append(new_teacher)
    
    with open('data.json', 'w') as f:
        json.dump(data, f)
    
    return True, "Teacher added successfully"
