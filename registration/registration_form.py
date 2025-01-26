import tkinter as tk
from tkinter import ttk, messagebox
from .data_validation import validate_registration_data, save_registration

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Student Registration")
        master.geometry('400x500')

        # Create main frame
        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(self.frame, text="Student Registration", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Student Name
        ttk.Label(self.frame, text="Full Name:").pack(anchor=tk.W, pady=5)
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack(fill=tk.X, pady=5)

        # Email
        ttk.Label(self.frame, text="Email:").pack(anchor=tk.W, pady=5)
        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.pack(fill=tk.X, pady=5)

        # Grade
        ttk.Label(self.frame, text="Grade:").pack(anchor=tk.W, pady=5)
        self.grade_entry = ttk.Entry(self.frame)
        self.grade_entry.pack(fill=tk.X, pady=5)

        # Submit Button
        submit_btn = ttk.Button(self.frame, text="Register", command=self.register)
        submit_btn.pack(pady=20)

        # Status Label
        self.status_label = ttk.Label(self.frame, text="")
        self.status_label.pack(pady=10)

    def register(self):
        # Get form data
        student_data = {
            'name': self.name_entry.get().strip(),
            'email': self.email_entry.get().strip(),
            'grade': self.grade_entry.get().strip()
        }

        # Validate data
        valid, message = validate_registration_data(student_data)
        if not valid:
            messagebox.showerror("Validation Error", message)
            return

        # Save registration
        success, message = save_registration(student_data)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
        else:
            messagebox.showerror("Error", message)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.name_entry.focus()

if __name__ == '__main__':
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
