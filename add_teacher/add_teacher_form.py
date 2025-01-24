import tkinter as tk
from tkinter import ttk, messagebox
import json

class AddTeacherForm:
    def __init__(self, master):
        self.master = master
        master.title("Add a New Teacher")
        master.geometry('400x300')  # Set window size

        # Create a frame for better organization
        frame = ttk.Frame(master, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(frame, text="Add a New Teacher", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Teacher Name Entry
        self.teacher_name_label = ttk.Label(frame, text="Teacher Name:")
        self.teacher_name_label.pack(pady=5)
        self.teacher_name_entry = ttk.Entry(frame, width=30)
        self.teacher_name_entry.pack(pady=5)

        # Teacher Email Entry
        self.teacher_email_label = ttk.Label(frame, text="Teacher Email:")
        self.teacher_email_label.pack(pady=5)
        self.teacher_email_entry = ttk.Entry(frame, width=30)
        self.teacher_email_entry.pack(pady=5)

        # Teacher Subject Entry
        self.teacher_subject_label = ttk.Label(frame, text="Teacher Subject:")
        self.teacher_subject_label.pack(pady=5)
        self.teacher_subject_entry = ttk.Entry(frame, width=30)
        self.teacher_subject_entry.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(frame, text="Add Teacher", command=self.submit)
        self.submit_button.pack(pady=20)

    def validate_data(self, name, email, subject):
        if not name or not email or not subject:
            messagebox.showerror("Error", "Please fill in all fields.")
            return False
        return True

    def submit(self):
        teacher_name = self.teacher_name_entry.get()
        teacher_email = self.teacher_email_entry.get()
        teacher_subject = self.teacher_subject_entry.get()
        if self.validate_data(teacher_name, teacher_email, teacher_subject):
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
                    if teacher_email in [teacher['email'] for teacher in data['teachers']]:
                        messagebox.showerror("Error", "Email already registered.")
                        return
            except FileNotFoundError:
                data = {'teachers': []}
            # Add the new teacher to the data
            data['teachers'].append({
                'id': len(data['teachers']) + 1,
                'name': teacher_name,
                'email': teacher_email,
                'subject': teacher_subject
            })
            with open('data.json', 'w') as f:
                json.dump(data, f)
            print("Teacher added successfully!")

if __name__ == '__main__':
    root = tk.Tk()
    add_teacher = AddTeacherForm(root)
    root.mainloop()
