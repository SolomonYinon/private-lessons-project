import tkinter as tk
from tkinter import ttk
import json

class PaymentTracking:
    def __init__(self, master):
        self.master = master
        master.title("Payment Tracking")
        master.geometry('400x300')

        # Title Label
        title_label = ttk.Label(master, text="Students Who Paid", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Listbox to display paid students
        self.paid_students_listbox = tk.Listbox(master, width=50)
        self.paid_students_listbox.pack(pady=20)

        self.load_paid_students()

    def load_paid_students(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                paid_students = [student for student in data['students'] if student['paid']]
                for student in paid_students:
                    self.paid_students_listbox.insert(tk.END, f"{student['name']} (ID: {student['id']})")
        except FileNotFoundError:
            print("Data file not found.")

if __name__ == '__main__':
    root = tk.Tk()
    app = PaymentTracking(root)
    root.mainloop()
