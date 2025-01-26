import tkinter as tk
from tkinter import ttk, messagebox
import json
from registration.data_validation import validate_data

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Registration Form")
        master.geometry('400x400')  # Set window size

        # Create a frame for better organization
        frame = ttk.Frame(master, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(frame, text="Register Here", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # ID Entry
        self.id_label = ttk.Label(frame, text="ID:")
        self.id_label.pack(pady=5)
        self.id_entry = ttk.Entry(frame, width=30)
        self.id_entry.pack(pady=5)

        # Name Entry
        self.name_label = ttk.Label(frame, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = ttk.Entry(frame, width=30)
        self.name_entry.pack(pady=5)

        # Email Entry
        self.email_label = ttk.Label(frame, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = ttk.Entry(frame, width=30)
        self.email_entry.pack(pady=5)

        # Password Entry
        self.password_label = ttk.Label(frame, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(frame, width=30, show='*')
        self.password_entry.pack(pady=5)

        # Submit Button
        self.submit_button = ttk.Button(frame, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if validate_data(name, email):
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
                    if email in [student['email'] for student in data['students']]:
                        tk.messagebox.showerror("Error", "Email already registered.")
                        return
            except FileNotFoundError:
                data = {'students': []}
            data['students'].append({
                'id': len(data['students']) + 1,
                'name': name,
                'email': email,
                'password': password,
                'registered': True,
                'paid': False
            })
            with open('data.json', 'w') as f:
                json.dump(data, f)
            print("Student added successfully!")
        else:
            print("Invalid data!")

if __name__ == '__main__':
    root = tk.Tk()
    form = RegistrationForm(root)
    root.mainloop()
