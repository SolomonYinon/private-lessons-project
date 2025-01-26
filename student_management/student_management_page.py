import tkinter as tk
from tkinter import ttk, messagebox
from .display_all_students_logic import get_all_students, update_student, delete_student

class StudentManagementPage:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        master.geometry('800x600')

        # Create main frame
        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(self.frame, text="Student Management", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Create Treeview
        self.tree = ttk.Treeview(self.frame, columns=('ID', 'Name', 'Email', 'Grade', 'Status'), show='headings')
        
        # Define headings
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Grade', text='Grade')
        self.tree.heading('Status', text='Status')
        
        # Define columns
        self.tree.column('ID', width=100)
        self.tree.column('Name', width=150)
        self.tree.column('Email', width=200)
        self.tree.column('Grade', width=100)
        self.tree.column('Status', width=100)
        
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Buttons Frame
        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(fill=tk.X, pady=10)

        # Add buttons
        ttk.Button(buttons_frame, text="Refresh", command=self.refresh_students).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Update", command=self.update_selected_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Delete", command=self.delete_selected_student).pack(side=tk.LEFT, padx=5)

        # Load students
        self.refresh_students()

    def refresh_students(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get and display students
        success, result = get_all_students()
        if success:
            for student in result:
                self.tree.insert('', tk.END, values=(
                    student['id'],
                    student['name'],
                    student['email'],
                    student['grade'],
                    student['status']
                ))
        else:
            messagebox.showerror("Error", result)

    def update_selected_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to update")
            return

        # Get current values
        values = self.tree.item(selected[0])['values']
        student_id = values[0]

        # Create update dialog
        dialog = tk.Toplevel(self.master)
        dialog.title("Update Student")
        dialog.geometry('400x300')

        # Create form fields
        ttk.Label(dialog, text="Name:").pack(pady=5)
        name_entry = ttk.Entry(dialog)
        name_entry.insert(0, values[1])
        name_entry.pack(pady=5)

        ttk.Label(dialog, text="Email:").pack(pady=5)
        email_entry = ttk.Entry(dialog)
        email_entry.insert(0, values[2])
        email_entry.pack(pady=5)

        ttk.Label(dialog, text="Grade:").pack(pady=5)
        grade_entry = ttk.Entry(dialog)
        grade_entry.insert(0, values[3])
        grade_entry.pack(pady=5)

        # Status dropdown
        ttk.Label(dialog, text="Status:").pack(pady=5)
        status_var = tk.StringVar(value=values[4])
        status_combo = ttk.Combobox(dialog, textvariable=status_var, values=['Active', 'Inactive'])
        status_combo.pack(pady=5)

        def save_changes():
            updated_data = {
                'name': name_entry.get(),
                'email': email_entry.get(),
                'grade': grade_entry.get(),
                'active': status_var.get() == 'Active'
            }
            
            success, message = update_student(student_id, updated_data)
            if success:
                messagebox.showinfo("Success", message)
                dialog.destroy()
                self.refresh_students()
            else:
                messagebox.showerror("Error", message)

        ttk.Button(dialog, text="Save", command=save_changes).pack(pady=20)

    def delete_selected_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to delete")
            return

        # Get student ID
        student_id = self.tree.item(selected[0])['values'][0]

        # Confirm deletion
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            success, message = delete_student(student_id)
            if success:
                messagebox.showinfo("Success", message)
                self.refresh_students()
            else:
                messagebox.showerror("Error", message)

if __name__ == '__main__':
    root = tk.Tk()
    app = StudentManagementPage(root)
    root.mainloop()
