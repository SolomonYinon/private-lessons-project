import tkinter as tk
from tkinter import ttk, messagebox
import json
from payment.payment_gateway_integration import integrate_payment_gateway

class PaymentInterface:
    def __init__(self, master):
        self.master = master
        master.title("Payment Interface")
        master.geometry('400x300')  # Set window size

        # Create a frame for better organization
        frame = ttk.Frame(master, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(frame, text="Payment Options", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Payment Options Listbox
        self.payment_options = tk.Listbox(frame, width=50)
        self.payment_options.pack(pady=10)

        self.load_payment_options()  # Load payment options from a data source
        self.payment_options.bind('<<ListboxSelect>>', self.on_option_select)
        self.selected_option = None

        # Login Button
        self.login_button = ttk.Button(frame, text="Login", command=self.login_user)
        self.login_button.pack(pady=20)

        # Sample Payment Button
        self.pay_button = ttk.Button(frame, text="Pay Now", command=self.process_payment)
        self.pay_button.pack(pady=20)

    def load_payment_options(self):
        try:
            with open('payment_options.json', 'r') as f:
                options = json.load(f)
                for option in options:
                    self.payment_options.insert(tk.END, option)
        except FileNotFoundError:
            print("No payment options found.")

    def on_option_select(self, event):
        selected_indices = self.payment_options.curselection()
        if selected_indices:
            self.selected_option = self.payment_options.get(selected_indices[0])
        else:
            self.selected_option = None

    def login_user(self):
        login_window = tk.Toplevel(self.master)
        login_window.title("Login")
        login_window.geometry('300x200')

        ttk.Label(login_window, text="Student ID:").pack(pady=5)
        self.student_id_entry = ttk.Entry(login_window)
        self.student_id_entry.pack(pady=5)

        ttk.Label(login_window, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(login_window, show='*')
        self.password_entry.pack(pady=5)

        ttk.Button(login_window, text="Login", command=self.check_login).pack(pady=20)

    def check_login(self):
        student_id = self.student_id_entry.get()
        password = self.password_entry.get()
        with open('data.json', 'r') as f:
            data = json.load(f)
            student = next((s for s in data['students'] if s['id'] == student_id and s['password'] == password), None)
            if student and not student['paid']:
                self.show_payment_form()
            else:
                tk.messagebox.showerror("Error", "Invalid credentials or already paid.")

    def show_payment_form(self):
        payment_window = tk.Toplevel(self.master)
        payment_window.title("Credit Card Payment")
        payment_window.geometry('400x300')

        ttk.Label(payment_window, text="Enter Credit Card Details:").pack(pady=10)

        ttk.Label(payment_window, text="Card Number:").pack(pady=5)
        self.card_number_entry = ttk.Entry(payment_window)
        self.card_number_entry.pack(pady=5)

        ttk.Label(payment_window, text="Expiration Date (MM/YY):").pack(pady=5)
        self.expiration_entry = ttk.Entry(payment_window)
        self.expiration_entry.pack(pady=5)

        ttk.Label(payment_window, text="CVV:").pack(pady=5)
        self.cvv_entry = ttk.Entry(payment_window)
        self.cvv_entry.pack(pady=5)

        ttk.Button(payment_window, text="Pay Now", command=self.process_payment).pack(pady=20)

    def process_payment(self):
        student_id = self.student_id_entry.get()
        with open('data.json', 'r') as f:
            data = json.load(f)
            student = next((s for s in data['students'] if s['id'] == student_id), None)
            if student:
                # Assuming payment is successful
                student['paid'] = True
                # Update the payments list
                payment_data = {
                    'student_id': student_id,
                    'amount': 100,
                    'date': "2025-01-09T12:51:11+02:00",
                    'method': "credit_card",
                    'status': "completed"
                }
                data['payments'].append(payment_data)
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                tk.messagebox.showinfo("Success", "Payment processed successfully!")
            else:
                tk.messagebox.showerror("Error", "Student not registered.")

if __name__ == '__main__':
    root = tk.Tk()
    payment = PaymentInterface(root)
    root.mainloop()
