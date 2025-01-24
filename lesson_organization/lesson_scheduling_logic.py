import json

def schedule_lessons(lesson_data):
    # Logic to schedule lessons
    try:
        with open('scheduled_lessons.json', 'a') as f:
            json.dump(lesson_data, f)
            f.write('\n')
        print(f"Lesson scheduled: {lesson_data}")
    except Exception as e:
        print(f"Error scheduling lesson: {e}")
