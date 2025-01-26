import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from .lesson_scheduling_logic import organize_lessons, get_teacher_schedule

class LessonOrganizationInterface:
    def __init__(self, master):
        self.master = master
        master.title("Lesson Organization")
        master.geometry('600x400')

        # Create main frame
        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(self.frame, text="Organize Lessons", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Teacher ID
        ttk.Label(self.frame, text="Teacher ID:").pack(anchor=tk.W, pady=5)
        self.teacher_id_entry = ttk.Entry(self.frame)
        self.teacher_id_entry.pack(fill=tk.X, pady=5)

        # Date Range Frame
        date_frame = ttk.LabelFrame(self.frame, text="Date Range", padding="10")
        date_frame.pack(fill=tk.X, pady=10)

        # Start Date
        ttk.Label(date_frame, text="Start Date (YYYY-MM-DD):").pack(anchor=tk.W, pady=5)
        self.start_date_entry = ttk.Entry(date_frame)
        self.start_date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.start_date_entry.pack(fill=tk.X, pady=5)

        # End Date
        ttk.Label(date_frame, text="End Date (YYYY-MM-DD):").pack(anchor=tk.W, pady=5)
        self.end_date_entry = ttk.Entry(date_frame)
        end_date = datetime.now() + timedelta(days=30)  # Default to 30 days from now
        self.end_date_entry.insert(0, end_date.strftime("%Y-%m-%d"))
        self.end_date_entry.pack(fill=tk.X, pady=5)

        # Organize Button
        ttk.Button(self.frame, text="Organize Lessons", command=self.organize_lessons).pack(pady=20)

        # Results Frame
        self.results_frame = ttk.LabelFrame(self.frame, text="Results", padding="10")
        self.results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Results Text
        self.results_text = tk.Text(self.results_frame, height=8, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True)

    def organize_lessons(self):
        try:
            teacher_id = int(self.teacher_id_entry.get().strip())
            start_date = self.start_date_entry.get().strip()
            end_date = self.end_date_entry.get().strip()

            # Validate dates
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
                return

            # Organize lessons
            success, message = organize_lessons(teacher_id, start_date, end_date)
            
            if success:
                messagebox.showinfo("Success", message)
                self.show_schedule(teacher_id)
            else:
                messagebox.showerror("Error", message)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid teacher ID")

    def show_schedule(self, teacher_id):
        success, lessons = get_teacher_schedule(teacher_id)
        if success:
            self.results_text.delete(1.0, tk.END)
            if lessons:
                self.results_text.insert(tk.END, "Scheduled Lessons:\n\n")
                for lesson in sorted(lessons, key=lambda x: (x['date'], x['time'])):
                    self.results_text.insert(tk.END, 
                        f"Date: {lesson['date']}\n"
                        f"Time: {lesson['time']}\n"
                        f"Student ID: {lesson['student_id']}\n"
                        f"Status: {lesson['status']}\n"
                        f"{'=' * 30}\n"
                    )
            else:
                self.results_text.insert(tk.END, "No lessons scheduled for this teacher.")
        else:
            self.results_text.insert(tk.END, f"Error: {lessons}")

if __name__ == '__main__':
    root = tk.Tk()
    app = LessonOrganizationInterface(root)
    root.mainloop()
