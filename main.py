from add_lesson.add_lesson_form import *
from add_teacher.add_teacher_form import *
from attendance.attendance_marking_interface import *
from payment_tracking.payment_tracking_page import *
from lesson_organization.lesson_organization_interface import *
from payment.payment_interface import *
from payment_tracking.payment_tracking_page import *
from registration.registration_form import *
from schedule.schedule_interface import *
from student_list.student_list_page import *
from student_management.student_management_page import *
import tkinter as tk
from tkinter import messagebox


def add_lesson():
    root = tk.Tk()
    add_lesson = AddLessonForm(root)
    root.mainloop()

def add_teacher():
    root = tk.Tk()
    add_teacher = AddTeacherForm(root)
    root.mainloop()

def mark_attendance():
    root = tk.Tk()
    mark_attendance = AttendanceMarkingInterface(root)
    root.mainloop()

def track_payment():
    root = tk.Tk()
    track_payment = PaymentTracking(root)
    root.mainloop()

def organize_lesson():
    root = tk.Tk()
    organize_lesson = LessonOrganizationInterface(root)
    root.mainloop()

def process_payment():
    root = tk.Tk()
    process_payment = PaymentInterface(root)
    root.mainloop()

def register_student():
    root = tk.Tk()
    register_student = RegistrationForm(root)
    root.mainloop()

def view_schedule():
    root = tk.Tk()
    view_schedule = ScheduleInterface(root)
    root.mainloop()

def list_students():
    root = tk.Tk()
    list_students = StudentListPage(root)
    root.mainloop()

def manage_student():
    root = tk.Tk()
    manage_student = StudentManagement(root)
    root.mainloop()

def main():
    root = tk.Tk()
    root.title("Private Lessons Project")

    def on_select(option):
        if option == '1':
            add_lesson()
        elif option == '2':
            add_teacher()
        elif option == '3':
            mark_attendance()
        elif option == '4':
            track_payment()
        elif option == '5':
            organize_lesson()
        elif option == '6':
            process_payment()
        elif option == '7':
            register_student()
        elif option == '8':
            view_schedule()
        elif option == '9':
            list_students()
        elif option == '10':
            manage_student()
        elif option == '11':
            root.quit()
        else:
            messagebox.showerror("Error", "Invalid choice, please try again.")

    options = [
        "1. Add Lesson",
        "2. Add Teacher",
        "3. Mark Attendance",
        "4. Track Payment",
        "5. Organize Lesson",
        "6. Process Payment",
        "7. Register Student",
        "8. View Schedule",
        "9. List Students",
        "10. Manage Student",
        "11. Exit"
    ]

    for option in options:
        button = tk.Button(root, text=option, command=lambda opt=option.split('.')[0]: on_select(opt))
        button.pack(fill='x')

    root.mainloop()

if __name__ == "__main__":
    main()