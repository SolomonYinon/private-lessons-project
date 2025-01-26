import tkinter as tk
from tkinter import ttk, messagebox
import json
from .teacher_student_display_logic import get_teacher_students, get_student_details

class StudentListPage:
    def __init__(self, master, teacher_id=None):
        self.master = master
        self.teacher_id = teacher_id
        master.title("Student List")
        master.geometry('800x600')

        # Create frame
        self.frame = ttk.Frame(master)
        self.frame.pack(pady=20)

        # Label for showing student info
        self.info_label = ttk.Label(self.frame, text="", wraplength=700)
        self.info_label.pack(pady=10)

        self.populate_student_list()

    def populate_student_list(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                students = data.get('students', [])  # Get all students
                if students:
                    student_names = [f"{student['name']} (ID: {student['id']})" for student in students]
                    self.info_label.config(text="Students:\n" + "\n".join(student_names))
                else:
                    self.info_label.config(text="No students found.")
        except Exception as e:
            self.info_label.config(text=f"Error loading students: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = StudentListPage(root)
    root.mainloop()
