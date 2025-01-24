import tkinter as tk
from tkinter import ttk, messagebox
import json

class StudentListPage:
    def __init__(self, master):
        self.master = master
        master.title("Student List")
        master.geometry('600x400')

        # Title Label
        title_label = ttk.Label(master, text="List of Students", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Treeview to display student details
        self.tree = ttk.Treeview(master, columns=("ID", "Name", "Email", "Registered", "Paid"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Registered", text="Registered")
        self.tree.heading("Paid", text="Paid")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Load student data
        self.load_students()

    def load_students(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for student in data['students']:
                    self.tree.insert("", tk.END, values=(student['id'], student['name'], student['email'], student['registered'], student['paid']))
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")

if __name__ == '__main__':
    root = tk.Tk()
    app = StudentListPage(root)
    root.mainloop()
