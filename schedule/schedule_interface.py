import tkinter as tk
from tkinter import ttk, messagebox
import json

class ScheduleInterface:
    def __init__(self, master):
        self.master = master
        master.title("Schedule")
        master.geometry('400x400')

        # Title Label
        title_label = ttk.Label(master, text="Scheduled Lessons", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Listbox to display lessons
        self.lesson_listbox = tk.Listbox(master, width=50)
        self.lesson_listbox.pack(pady=20)

        # Edit Button
        self.edit_button = ttk.Button(master, text="Edit Selected", command=self.edit_lesson)
        self.edit_button.pack(pady=10)

        # Load lessons
        self.load_lessons()

    def load_lessons(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for lesson in data['lessons']:
                    teacher_name = next((t['name'] for t in data['teachers'] if t['id'] == lesson['teacher_id']), "Unknown Teacher")
                    lesson_display = f"{lesson['name']} (ID: {lesson['id']})"
                    print(lesson_display)  # Debugging: print the lesson display string
                    self.lesson_listbox.insert(tk.END, lesson_display)
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")

    def edit_lesson(self):
        selected_index = self.lesson_listbox.curselection()
        if selected_index:
            selected_lesson = self.lesson_listbox.get(selected_index[0])
            try:
                lesson_id = selected_lesson.split(' (ID: ')[1][:-1]  # Extract ID
                self.open_edit_window(lesson_id)
            except IndexError:
                messagebox.showerror("Error", "Selected lesson format is incorrect.")
        else:
            messagebox.showerror("Error", "No lesson selected.")

    def open_edit_window(self, lesson_id):
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Lesson")

        # Load lesson data
        with open('data.json', 'r') as f:
            data = json.load(f)
            lesson = next((l for l in data['lessons'] if l['id'] == int(lesson_id)), None)

        # Create fields for editing
        ttk.Label(edit_window, text="Lesson Name:").pack(pady=5)
        name_entry = ttk.Entry(edit_window)
        name_entry.insert(0, lesson['name'])
        name_entry.pack(pady=5)

        ttk.Label(edit_window, text="Schedule:").pack(pady=5)
        schedule_entry = ttk.Entry(edit_window)
        schedule_entry.insert(0, lesson['schedule'])
        schedule_entry.pack(pady=5)

        # Teacher Selection
        ttk.Label(edit_window, text="Select Teacher:").pack(pady=5)
        teacher_combobox = ttk.Combobox(edit_window)
        self.load_teachers(teacher_combobox, lesson['teacher_id'])
        teacher_combobox.pack(pady=5)

        # Student Selection
        ttk.Label(edit_window, text="Select Students (comma separated IDs):").pack(pady=5)
        student_entry = ttk.Entry(edit_window)
        student_entry.insert(0, ', '.join(lesson['student_ids']))  # Pre-fill with current student IDs
        student_entry.pack(pady=5)

        ttk.Button(edit_window, text="Save", command=lambda: self.save_changes(lesson_id, name_entry.get(), schedule_entry.get(), teacher_combobox.get(), student_entry.get())).pack(pady=20)

    def load_teachers(self, teacher_combobox, selected_teacher_id):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                teachers = [f"{teacher['name']} (ID: {teacher['id']})" for teacher in data['teachers']]
                teacher_combobox['values'] = teachers
                # Set the selected teacher
                if selected_teacher_id:
                    selected_teacher = next((t for t in data['teachers'] if t['id'] == selected_teacher_id), None)
                    if selected_teacher:
                        teacher_combobox.set(f"{selected_teacher['name']} (ID: {selected_teacher['id']})")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")

    def save_changes(self, lesson_id, name, schedule, teacher, students):
        with open('data.json', 'r') as f:
            data = json.load(f)
            lesson = next((l for l in data['lessons'] if l['id'] == int(lesson_id)), None)
            if lesson:
                lesson['name'] = name
                lesson['schedule'] = schedule
                lesson['teacher_id'] = teacher.split(' (ID: ')[1][:-1]  # Extract teacher ID
                lesson['student_ids'] = [s.strip() for s in students.split(',')]  # Update student IDs

        with open('data.json', 'w') as f:
            json.dump(data, f)
        messagebox.showinfo("Success", "Lesson details updated!")

if __name__ == '__main__':
    root = tk.Tk()
    app = ScheduleInterface(root)
    root.mainloop()
