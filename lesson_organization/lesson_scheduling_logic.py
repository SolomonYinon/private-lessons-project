import json
from datetime import datetime, timedelta

def get_teacher_schedule(teacher_id):
    """Get all scheduled lessons for a teacher"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            lessons = [l for l in data.get('lessons', []) if l['teacher_id'] == teacher_id]
            return True, lessons
    except FileNotFoundError:
        return False, "No schedule data found"
    except Exception as e:
        return False, f"Error retrieving schedule: {str(e)}"

def get_available_slots(teacher_id, date):
    """Get available time slots for a teacher on a specific date"""
    success, lessons = get_teacher_schedule(teacher_id)
    if not success:
        return False, lessons

    # Define working hours (8 AM to 8 PM)
    work_start = datetime.strptime("08:00", "%H:%M")
    work_end = datetime.strptime("20:00", "%H:%M")
    slot_duration = timedelta(minutes=60)

    # Get all occupied slots for the date
    occupied_slots = []
    for lesson in lessons:
        if lesson['date'] == date:
            lesson_time = datetime.strptime(lesson['time'], "%H:%M")
            occupied_slots.append(lesson_time)

    # Find available slots
    available_slots = []
    current_slot = work_start
    while current_slot + slot_duration <= work_end:
        if current_slot not in occupied_slots:
            available_slots.append(current_slot.strftime("%H:%M"))
        current_slot += slot_duration

    return True, available_slots

def organize_lessons(teacher_id, start_date, end_date):
    """Organize lessons for a teacher within a date range"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Get teacher details
        teacher = next((t for t in data.get('teachers', []) if t['id'] == teacher_id), None)
        if not teacher:
            return False, "Teacher not found"

        # Get all unscheduled students for this teacher's subject
        unscheduled_students = []
        for student in data.get('students', []):
            if student['active'] and student['registered'] and not any(
                l['student_id'] == student['id'] and 
                l['teacher_id'] == teacher_id and
                start_date <= l['date'] <= end_date
                for l in data.get('lessons', [])
            ):
                unscheduled_students.append(student)

        # Schedule lessons
        current_date = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        scheduled_lessons = []

        while current_date <= end and unscheduled_students:
            date_str = current_date.strftime("%Y-%m-%d")
            success, available_slots = get_available_slots(teacher_id, date_str)
            
            if success and available_slots:
                for slot in available_slots:
                    if not unscheduled_students:
                        break

                    student = unscheduled_students.pop(0)
                    new_lesson = {
                        'id': len(data.get('lessons', [])) + len(scheduled_lessons) + 1,
                        'name': teacher['subject'],
                        'teacher_id': teacher_id,
                        'student_id': student['id'],
                        'date': date_str,
                        'time': slot,
                        'duration': 60,
                        'status': 'scheduled'
                    }
                    scheduled_lessons.append(new_lesson)

            current_date += timedelta(days=1)

        # Save the new lessons
        if scheduled_lessons:
            if 'lessons' not in data:
                data['lessons'] = []
            data['lessons'].extend(scheduled_lessons)
            
            with open('data.json', 'w') as f:
                json.dump(data, f)

            return True, f"Successfully scheduled {len(scheduled_lessons)} lessons"
        else:
            return False, "No lessons could be scheduled"

    except Exception as e:
        return False, f"Error organizing lessons: {str(e)}"
