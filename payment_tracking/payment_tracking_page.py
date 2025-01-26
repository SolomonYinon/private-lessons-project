import tkinter as tk
from tkinter import ttk
from .payment_data_display_logic import get_payment_data, get_payment_summary

class PaymentTrackingPage:
    def __init__(self, master):
        self.master = master
        master.title("Payment Tracking")
        master.geometry('500x600')  # Set window size

        # Create frame
        self.frame = ttk.Frame(master, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(self.frame, text="Payment Tracking", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Summary Frame
        summary_frame = ttk.LabelFrame(self.frame, text="Payment Summary", padding="10")
        summary_frame.pack(fill=tk.X, pady=10)

        self.total_amount_label = ttk.Label(summary_frame, text="Total Amount: $0")
        self.total_amount_label.pack(side=tk.LEFT, padx=10)

        self.total_students_label = ttk.Label(summary_frame, text="Paid Students: 0")
        self.total_students_label.pack(side=tk.LEFT, padx=10)

        # Create Treeview
        self.tree = ttk.Treeview(self.frame, columns=('ID', 'Name', 'Amount', 'Date'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Amount', text='Amount')
        self.tree.heading('Date', text='Payment Date')
        
        # Configure column widths
        self.tree.column('ID', width=50)
        self.tree.column('Name', width=150)
        self.tree.column('Amount', width=100)
        self.tree.column('Date', width=100)
        
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Refresh Button
        refresh_btn = ttk.Button(self.frame, text="Refresh", command=self.load_data)
        refresh_btn.pack(pady=10)

        # Load initial data
        self.load_data()

    def load_data(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get and display payment data
        payments = get_payment_data()
        for payment in payments:
            self.tree.insert('', tk.END, values=(
                payment['id'],
                payment['name'],
                f"${payment['amount']:.2f}",
                payment['date']
            ))

        # Update summary
        summary = get_payment_summary()
        self.total_amount_label.config(text=f"Total Amount: ${summary['total_amount']:.2f}")
        self.total_students_label.config(text=f"Paid Students: {summary['total_students']}")

if __name__ == '__main__':
    root = tk.Tk()
    app = PaymentTrackingPage(root)
    root.mainloop()
