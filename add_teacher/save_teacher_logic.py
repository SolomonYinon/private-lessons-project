import json

def save_teacher(teacher_data):
    # Logic to save new teacher data
    try:
        with open('teachers.json', 'a') as f:
            json.dump(teacher_data, f)
            f.write('\n')
        print("Teacher saved!")
    except Exception as e:
        print(f"Error saving teacher: {e}")
