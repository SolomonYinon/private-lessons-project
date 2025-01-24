import tkinter as tk
from tkinter import ttk, messagebox
import json

class StudentManagement:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        master.geometry('400x400')

        # Title Label
        title_label = ttk.Label(master, text="All Students", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Listbox to display students
        self.student_listbox = tk.Listbox(master, width=50)
        self.student_listbox.pack(pady=20)

        # Load students
        self.load_students()

        # Edit Button
        self.edit_button = ttk.Button(master, text="Edit Selected", command=self.edit_student)
        self.edit_button.pack(pady=10)

    def load_students(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for student in data['students']:
                    self.student_listbox.insert(tk.END, f"{student['name']} (ID: {student['id']})")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")

    def edit_student(self):
        selected_index = self.student_listbox.curselection()
        if selected_index:
            selected_student = self.student_listbox.get(selected_index[0])
            student_id = selected_student.split(' (ID: ')[1][:-1]  # Extract ID
            self.open_edit_window(student_id)
        else:
            messagebox.showerror("Error", "No student selected.")

    def open_edit_window(self, student_id):
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Student")

        # Load student data
        with open('data.json', 'r') as f:
            data = json.load(f)
            student = next((s for s in data['students'] if s['id'] == student_id), None)

        # Create fields for editing
        ttk.Label(edit_window, text="Name:").pack(pady=5)
        name_entry = ttk.Entry(edit_window)
        name_entry.insert(0, student['name'])
        name_entry.pack(pady=5)

        ttk.Label(edit_window, text="Email:").pack(pady=5)
        email_entry = ttk.Entry(edit_window)
        email_entry.insert(0, student['email'])
        email_entry.pack(pady=5)

        ttk.Button(edit_window, text="Save", command=lambda: self.save_changes(student_id, name_entry.get(), email_entry.get())).pack(pady=20)

    def save_changes(self, student_id, name, email):
        with open('data.json', 'r') as f:
            data = json.load(f)
            student = next((s for s in data['students'] if s['id'] == student_id), None)
            if student:
                student['name'] = name
                student['email'] = email

        with open('data.json', 'w') as f:
            json.dump(data, f)
        messagebox.showinfo("Success", "Student details updated!")

if __name__ == '__main__':
    root = tk.Tk()
    app = StudentManagement(root)
    root.mainloop()
