import tkinter as tk
from tkinter import ttk, messagebox
from .save_teacher_logic import save_teacher

class AddTeacherForm:
    def __init__(self, master):
        self.master = master
        master.title("Add Teacher")
        master.geometry('400x400')

        # Create frame
        self.frame = ttk.Frame(master, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(self.frame, text="Add New Teacher", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Teacher Name
        ttk.Label(self.frame, text="Name:").pack(pady=5)
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack(pady=5)

        # Teacher Email
        ttk.Label(self.frame, text="Email:").pack(pady=5)
        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.pack(pady=5)

        # Teacher Subject
        ttk.Label(self.frame, text="Subject:").pack(pady=5)
        self.subject_entry = ttk.Entry(self.frame)
        self.subject_entry.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(self.frame, text="Add Teacher", command=self.save)
        self.submit_button.pack(pady=20)

    def save(self):
        if not self.validate_inputs():
            return

        teacher_data = {
            'name': self.name_entry.get(),
            'email': self.email_entry.get(),
            'subject': self.subject_entry.get()
        }

        success, message = save_teacher(teacher_data)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_inputs()
        else:
            messagebox.showerror("Error", message)

    def validate_inputs(self):
        if not all([self.name_entry.get(), self.email_entry.get(), self.subject_entry.get()]):
            messagebox.showerror("Error", "Please fill in all fields")
            return False
        return True

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = AddTeacherForm(root)
    root.mainloop()
