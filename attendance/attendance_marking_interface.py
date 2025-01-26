import tkinter as tk
import json
from tkinter import ttk
from attendance.attendance_update_logic import update_attendance

class AttendanceMarkingInterface:
    def __init__(self, master):
        self.master = master
        master.title("Attendance Marking")
        master.geometry('400x300')  # Set window size

        # Create a frame for better organization
        frame = ttk.Frame(master, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(frame, text="Mark Attendance", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Student ID Entry
        self.student_id_label = ttk.Label(frame, text="Student ID:")
        self.student_id_label.pack(pady=5)
        self.student_id_entry = ttk.Entry(frame, width=30)
        self.student_id_entry.pack(pady=5)

        # Attendance Status Dropdown
        self.attendance_status_label = ttk.Label(frame, text="Attendance Status:")
        self.attendance_status_label.pack(pady=5)
        self.attendance_status = tk.StringVar(frame)
        self.attendance_status.set("Present")  # default value
        self.attendance_status_option = ttk.OptionMenu(frame, self.attendance_status, "Present", "Absent")
        self.attendance_status_option.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(frame, text="Mark Attendance", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        student_id = self.student_id_entry.get()
        status = self.attendance_status.get()
        update_attendance(student_id, status)  # Call update logic
        print("Attendance marked!")

if __name__ == '__main__':
    root = tk.Tk()
    attendance = AttendanceMarkingInterface(root)
    root.mainloop()
