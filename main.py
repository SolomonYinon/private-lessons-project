import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import ttk, messagebox

# Import all interface classes
from registration.registration_form import RegistrationForm
from student_management.student_management_page import StudentManagementPage
from schedule.schedule_interface import ScheduleInterface
from payment.payment_interface import PaymentInterface
from lesson_organization.lesson_organization_interface import LessonOrganizationInterface
from attendance.attendance_marking_interface import AttendanceMarkingInterface
from add_lesson.add_lesson_form import AddLessonForm
from add_teacher.add_teacher_form import AddTeacherForm
from payment_tracking.payment_tracking_page import PaymentTrackingPage
from student_list.student_list_page import StudentListPage

class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("Private Lessons Project")
        master.geometry('800x600')

        # Create main frame
        main_frame = ttk.Frame(master, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(main_frame, text="Private Lessons Project", font=("Helvetica", 24))
        title_label.pack(pady=20)

        # Create buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(expand=True)

        # Button styles
        style = ttk.Style()
        style.configure('Action.TButton', padding=10)

        # Create buttons
        buttons = [
            ("Add Lesson", self.add_lesson),
            ("Add Teacher", self.add_teacher),
            ("Mark Attendance", self.mark_attendance),
            ("Track Payment", self.track_payment),
            ("Organize Lessons", self.organize_lessons),
            ("Process Payment", self.process_payment),
            ("Register Student", self.register_student),
            ("View Schedule", self.view_schedule),
            ("List Students", self.list_students),
            ("Manage Student", self.manage_students),
            ("Exit", self.exit)
        ]

        # Add buttons to frame
        for text, command in buttons:
            btn = ttk.Button(buttons_frame, text=text, command=command, style='Action.TButton')
            btn.pack(fill=tk.X, pady=5)

    def add_lesson(self):
        window = tk.Toplevel(self.master)
        AddLessonForm(window)

    def add_teacher(self):
        window = tk.Toplevel(self.master)
        AddTeacherForm(window)

    def mark_attendance(self):
        window = tk.Toplevel(self.master)
        AttendanceMarkingInterface(window)

    def track_payment(self):
        window = tk.Toplevel(self.master)
        PaymentTrackingPage(window)

    def organize_lessons(self):
        window = tk.Toplevel(self.master)
        LessonOrganizationInterface(window)

    def process_payment(self):
        window = tk.Toplevel(self.master)
        PaymentInterface(window)

    def register_student(self):
        window = tk.Toplevel(self.master)
        RegistrationForm(window)

    def view_schedule(self):
        window = tk.Toplevel(self.master)
        ScheduleInterface(window)

    def list_students(self):
        window = tk.Toplevel(self.master)
        StudentListPage(window)

    def manage_students(self):
        window = tk.Toplevel(self.master)
        StudentManagementPage(window)

    def exit(self):
        self.master.quit()

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()