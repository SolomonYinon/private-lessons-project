import tkinter as tk
import json
from tkinter import ttk, messagebox

class AddLessonForm:
    def __init__(self, master):
        self.master = master
        master.title("Add Lesson")
        master.geometry('400x400')

        # Lesson Title Entry
        self.lesson_title_label = ttk.Label(master, text="Lesson Title:")
        self.lesson_title_label.pack(pady=5)
        self.lesson_title_entry = ttk.Entry(master)
        self.lesson_title_entry.pack(pady=5)

        # Teacher Selection
        self.teacher_label = ttk.Label(master, text="Select Teacher:")
        self.teacher_label.pack(pady=5)
        self.teacher_combobox = ttk.Combobox(master)
        self.load_teachers()
        self.teacher_combobox.pack(pady=5)

        # Student Selection
        self.student_label = ttk.Label(master, text="Select Students (comma separated IDs):")
        self.student_label.pack(pady=5)
        self.student_entry = ttk.Entry(master)
        self.student_entry.pack(pady=5)

        # Schedule Entry
        self.schedule_label = ttk.Label(master, text="Schedule (YYYY-MM-DD HH:MM):")
        self.schedule_label.pack(pady=5)
        self.schedule_entry = ttk.Entry(master)
        self.schedule_entry.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(master, text="Add Lesson", command=self.submit)
        self.submit_button.pack(pady=20)

    def load_teachers(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                teachers = [f"{teacher['name']} (ID: {teacher['id']})" for teacher in data['teachers']]
                self.teacher_combobox['values'] = teachers
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")

    def submit(self):
        title = self.lesson_title_entry.get()
        teacher = self.teacher_combobox.get()
        students = self.student_entry.get().split(',')  # Get student IDs
        schedule = self.schedule_entry.get()

        if title and teacher and students and schedule:
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {'lessons': []}

            # Extract teacher ID from the selected teacher string
            teacher_id = teacher.split(' (ID: ')[1][:-1]  # Get the ID from the string

            # Add the new lesson to the data
            data['lessons'].append({
                'id': len(data['lessons']) + 1,
                'name': title,
                'teacher_id': teacher_id,
                'student_ids': [s.strip() for s in students],
                'schedule': schedule
            })

            with open('data.json', 'w') as f:
                json.dump(data, f)
            messagebox.showinfo("Success", "Lesson added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

if __name__ == '__main__':
    root = tk.Tk()
    add_lesson = AddLessonForm(root)
    root.mainloop()
