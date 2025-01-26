import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from project.payment.payment_gateway_integration import process_payment, get_payment_history

class PaymentInterface:
    def __init__(self, master):
        self.master = master
        master.title("Payment Processing")
        master.geometry('800x600')

        # Create main frame
        self.frame = ttk.Frame(master, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(self.frame, text="Process Payment", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Student ID
        ttk.Label(self.frame, text="Student ID:").pack(anchor=tk.W, pady=5)
        self.student_id_entry = ttk.Entry(self.frame)
        self.student_id_entry.pack(fill=tk.X, pady=5)

        # Amount
        ttk.Label(self.frame, text="Amount:").pack(anchor=tk.W, pady=5)
        self.amount_entry = ttk.Entry(self.frame)
        self.amount_entry.pack(fill=tk.X, pady=5)

        # Payment Method
        ttk.Label(self.frame, text="Payment Method:").pack(anchor=tk.W, pady=5)
        self.payment_method = ttk.Combobox(self.frame, values=['Cash', 'Credit Card', 'Bank Transfer'])
        self.payment_method.set('Cash')
        self.payment_method.pack(fill=tk.X, pady=5)

        # Process Button
        ttk.Button(self.frame, text="Process Payment", command=self.process_payment).pack(pady=20)

        # Payment History
        history_label = ttk.Label(self.frame, text="Payment History", font=("Helvetica", 12))
        history_label.pack(pady=10)

        # Create Treeview for payment history
        columns = ('Date', 'Student ID', 'Amount', 'Method', 'Status')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')
        
        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Load initial payment history
        self.load_payment_history()

    def process_payment(self):
        try:
            student_id = int(self.student_id_entry.get().strip())
            amount = float(self.amount_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Invalid student ID or amount")
            return

        payment_data = {
            'student_id': student_id,
            'amount': amount,
            'payment_method': self.payment_method.get(),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        success, message = process_payment(payment_data)
        if success:
            messagebox.showinfo("Success", message)
            self.clear_form()
            self.load_payment_history()
        else:
            messagebox.showerror("Error", message)

    def load_payment_history(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get payment history
        success, payments = get_payment_history()
        if success:
            for payment in payments:
                self.tree.insert('', tk.END, values=(
                    payment['date'],
                    payment['student_id'],
                    f"${payment['amount']:.2f}",
                    payment['payment_method'],
                    payment['status']
                ))
        else:
            messagebox.showwarning("Warning", payments)

    def clear_form(self):
        self.student_id_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.payment_method.set('Cash')
        self.student_id_entry.focus()

if __name__ == '__main__':
    root = tk.Tk()
    app = PaymentInterface(root)
    root.mainloop()
