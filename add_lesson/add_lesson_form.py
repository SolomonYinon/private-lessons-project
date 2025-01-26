import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from .save_lesson_logic import save_lesson, get_teachers

class AddLessonForm:
    def __init__(self, master):
        self.master = master
        master.title("Add Lesson")
        master.geometry('500x600')

        # Create main frame
        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(self.frame, text="Schedule New Lesson", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Teacher Selection
        ttk.Label(self.frame, text="Select Teacher:").pack(anchor=tk.W, pady=5)
        self.teacher_var = tk.StringVar()
        self.teacher_combo = ttk.Combobox(self.frame, textvariable=self.teacher_var)
        self.teacher_combo.pack(fill=tk.X, pady=5)

        # Subject
        ttk.Label(self.frame, text="Subject:").pack(anchor=tk.W, pady=5)
        self.subject_entry = ttk.Entry(self.frame)
        self.subject_entry.pack(fill=tk.X, pady=5)

        # Student ID
        ttk.Label(self.frame, text="Student ID:").pack(anchor=tk.W, pady=5)
        self.student_id_entry = ttk.Entry(self.frame)
        self.student_id_entry.pack(fill=tk.X, pady=5)

        # Date Frame
        date_frame = ttk.LabelFrame(self.frame, text="Date and Time", padding="10")
        date_frame.pack(fill=tk.X, pady=10)

        # Date
        ttk.Label(date_frame, text="Date (YYYY-MM-DD):").pack(anchor=tk.W, pady=5)
        self.date_entry = ttk.Entry(date_frame)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.pack(fill=tk.X, pady=5)

        # Time
        ttk.Label(date_frame, text="Time (HH:MM):").pack(anchor=tk.W, pady=5)
        self.time_entry = ttk.Entry(date_frame)
        self.time_entry.insert(0, "09:00")
        self.time_entry.pack(fill=tk.X, pady=5)

        # Submit Button
        ttk.Button(self.frame, text="Schedule Lesson", command=self.submit).pack(pady=20)

        # Load teachers
        self.load_teachers()

    def load_teachers(self):
        success, result = get_teachers()
        if success:
            teacher_list = [f"{t['id']} - {t['name']} ({t['subject']})" for t in result]
            self.teacher_combo['values'] = teacher_list
            if teacher_list:
                self.teacher_combo.set(teacher_list[0])
        else:
            messagebox.showerror("Error", result)

    def submit(self):
        try:
            # Validate inputs
            if not all([self.teacher_var.get(), self.subject_entry.get(), 
                       self.student_id_entry.get(), self.date_entry.get(), 
                       self.time_entry.get()]):
                messagebox.showwarning("Warning", "Please fill in all fields")
                return

            # Extract teacher ID from combo selection
            teacher_id = self.teacher_var.get().split(' - ')[0]

            # Create lesson data
            lesson_data = {
                'teacher_id': teacher_id,
                'subject': self.subject_entry.get(),
                'student_id': self.student_id_entry.get(),
                'schedule': f"{self.date_entry.get()} {self.time_entry.get()}"
            }

            # Save lesson
            success, message = save_lesson(lesson_data)
            if success:
                messagebox.showinfo("Success", message)
                self.master.destroy()
            else:
                messagebox.showerror("Error", message)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to schedule lesson: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = AddLessonForm(root)
    root.mainloop()
