import json

def update_attendance(student_id, status):
    # Logic to update attendance status
    try:
        with open('attendance.json', 'r+') as f:
            attendance_data = json.load(f)
            attendance_data[student_id] = status  # Update the status for the student
            f.seek(0)
            json.dump(attendance_data, f)
            f.truncate()  # Remove old data
        print(f"Attendance for student {student_id} updated to {status}.")
    except FileNotFoundError:
        print("Attendance file not found.")
    except Exception as e:
        print(f"Error updating attendance: {e}")
