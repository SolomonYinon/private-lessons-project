import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from .lesson_display_logic import get_lessons, add_lesson, update_lesson_status

class ScheduleInterface:
    def __init__(self, master):
        self.master = master
        master.title("Lesson Schedule")
        master.geometry('800x600')

        # Create main frame
        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.schedule_tab = ttk.Frame(self.notebook)
        self.add_lesson_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.schedule_tab, text='View Schedule')
        self.notebook.add(self.add_lesson_tab, text='Add Lesson')

        # Setup schedule view
        self.setup_schedule_view()
        
        # Setup add lesson form
        self.setup_add_lesson_form()

    def setup_schedule_view(self):
        # Filter Frame
        filter_frame = ttk.LabelFrame(self.schedule_tab, text="Filters", padding="10")
        filter_frame.pack(fill=tk.X, pady=10)

        # Date Filter
        ttk.Label(filter_frame, text="Date:").pack(side=tk.LEFT, padx=5)
        self.date_entry = ttk.Entry(filter_frame, width=10)
        self.date_entry.pack(side=tk.LEFT, padx=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Teacher Filter
        ttk.Label(filter_frame, text="Teacher ID:").pack(side=tk.LEFT, padx=5)
        self.teacher_filter = ttk.Entry(filter_frame, width=10)
        self.teacher_filter.pack(side=tk.LEFT, padx=5)

        # Student Filter
        ttk.Label(filter_frame, text="Student ID:").pack(side=tk.LEFT, padx=5)
        self.student_filter = ttk.Entry(filter_frame, width=10)
        self.student_filter.pack(side=tk.LEFT, padx=5)

        # Apply Filter Button
        ttk.Button(filter_frame, text="Apply Filters", command=self.refresh_schedule).pack(side=tk.LEFT, padx=20)

        # Schedule Treeview
        columns = ('ID', 'Date', 'Time', 'Teacher', 'Student', 'Duration', 'Status')
        self.tree = ttk.Treeview(self.schedule_tab, columns=columns, show='headings')
        
        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.schedule_tab, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Status Update Frame
        status_frame = ttk.Frame(self.schedule_tab)
        status_frame.pack(fill=tk.X, pady=10)

        self.status_combo = ttk.Combobox(status_frame, values=['scheduled', 'completed', 'cancelled'])
        self.status_combo.set('completed')
        self.status_combo.pack(side=tk.LEFT, padx=5)

        ttk.Button(status_frame, text="Update Status", command=self.update_status).pack(side=tk.LEFT, padx=5)

        # Initial load
        self.refresh_schedule()

    def setup_add_lesson_form(self):
        # Create form frame
        form_frame = ttk.Frame(self.add_lesson_tab, padding="20")
        form_frame.pack(fill=tk.BOTH, expand=True)

        # Teacher ID
        ttk.Label(form_frame, text="Teacher ID:").pack(anchor=tk.W, pady=5)
        self.teacher_id_entry = ttk.Entry(form_frame)
        self.teacher_id_entry.pack(fill=tk.X, pady=5)

        # Student ID
        ttk.Label(form_frame, text="Student ID:").pack(anchor=tk.W, pady=5)
        self.student_id_entry = ttk.Entry(form_frame)
        self.student_id_entry.pack(fill=tk.X, pady=5)

        # Date
        ttk.Label(form_frame, text="Date (YYYY-MM-DD):").pack(anchor=tk.W, pady=5)
        self.date_entry = ttk.Entry(form_frame)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.pack(fill=tk.X, pady=5)

        # Time
        ttk.Label(form_frame, text="Time (HH:MM):").pack(anchor=tk.W, pady=5)
        self.time_entry = ttk.Entry(form_frame)
        self.time_entry.insert(0, datetime.now().strftime("%H:%M"))
        self.time_entry.pack(fill=tk.X, pady=5)

        # Duration (minutes)
        ttk.Label(form_frame, text="Duration (minutes):").pack(anchor=tk.W, pady=5)
        self.duration_entry = ttk.Entry(form_frame)
        self.duration_entry.insert(0, "60")
        self.duration_entry.pack(fill=tk.X, pady=5)

        # Add Button
        ttk.Button(form_frame, text="Schedule Lesson", command=self.schedule_lesson).pack(pady=20)

    def refresh_schedule(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get filter values
        teacher_id = self.teacher_filter.get().strip()
        student_id = self.student_filter.get().strip()
        date = self.date_entry.get().strip()

        # Convert IDs to int if provided
        teacher_id = int(teacher_id) if teacher_id else None
        student_id = int(student_id) if student_id else None

        # Get lessons
        success, lessons = get_lessons(teacher_id, student_id, date)
        if success:
            for lesson in lessons:
                self.tree.insert('', tk.END, values=(
                    lesson['id'],
                    lesson['date'],
                    lesson['time'],
                    lesson['teacher_id'],
                    lesson['student_id'],
                    f"{lesson['duration']} min",
                    lesson['status']
                ))
        else:
            messagebox.showwarning("Warning", lessons)

    def schedule_lesson(self):
        try:
            lesson_data = {
                'teacher_id': int(self.teacher_id_entry.get().strip()),
                'student_id': int(self.student_id_entry.get().strip()),
                'date': self.date_entry.get().strip(),
                'time': self.time_entry.get().strip(),
                'duration': int(self.duration_entry.get().strip())
            }
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for IDs and duration")
            return

        success, message = add_lesson(lesson_data)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
            self.notebook.select(0)  # Switch to schedule view
            self.refresh_schedule()
        else:
            messagebox.showerror("Error", message)

    def update_status(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a lesson to update")
            return

        lesson_id = int(self.tree.item(selected_item[0])['values'][0])
        new_status = self.status_combo.get()

        success, message = update_lesson_status(lesson_id, new_status)
        if success:
            messagebox.showinfo("Success", message)
            self.refresh_schedule()
        else:
            messagebox.showerror("Error", message)

    def clear_form(self):
        self.teacher_id_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, datetime.now().strftime("%H:%M"))
        self.duration_entry.delete(0, tk.END)
        self.duration_entry.insert(0, "60")

if __name__ == '__main__':
    root = tk.Tk()
    app = ScheduleInterface(root)
    root.mainloop()
