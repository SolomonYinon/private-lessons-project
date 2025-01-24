import json

def save_lesson(lesson_data):
    # Logic to save the new lesson data
    try:
        with open('lessons.json', 'a') as f:
            json.dump(lesson_data, f)
            f.write('\n')
        print("Lesson saved!")
    except Exception as e:
        print(f"Error saving lesson: {e}")
