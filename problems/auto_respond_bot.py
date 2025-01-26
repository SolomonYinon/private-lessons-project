import tkinter as tk
from tkinter import ttk, messagebox

# Predefined responses based on keywords
responses = {
    "payment issue": "Please check your payment details or contact support.",
    "schedule": "You can view your schedule in the 'View Schedule' section.",
    "registration": "To register, go to the 'Register Student' section.",
    "attendance": "Attendance can be marked in the 'Mark Attendance' section.",
    "lesson": "Lessons can be organized in the 'Organize Lessons' section."
}

class InquirySystem:
    def __init__(self, master):
        self.master = master
        master.title("User Inquiry System")
        master.geometry('600x400')

        # Title Label
        ttk.Label(master, text="Submit an Inquiry", font=("Helvetica", 16)).pack(pady=10)

        # Inquiry Entry
        ttk.Label(master, text="Enter your inquiry:").pack(anchor=tk.W, pady=5)
        self.inquiry_entry = ttk.Entry(master, width=70)
        self.inquiry_entry.pack(pady=5)

        # Submit Button
        ttk.Button(master, text="Submit", command=self.process_inquiry).pack(pady=10)

        # Response Label
        self.response_label = ttk.Label(master, text="", font=("Helvetica", 12), wraplength=500)
        self.response_label.pack(pady=20)

        # Inquiry Tracking Section
        ttk.Label(master, text="Inquiry History", font=("Helvetica", 14)).pack(pady=10)
        self.tree = ttk.Treeview(master, columns=("Inquiry", "Response"), show='headings')
        self.tree.heading("Inquiry", text="Inquiry")
        self.tree.heading("Response", text="Response")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
        
    def process_inquiry(self):
        inquiry = self.inquiry_entry.get().lower()
        
        # Check for predefined responses
        response = "Sorry, I couldn't understand your inquiry."  # Default response
        for keyword, reply in responses.items():
            if keyword in inquiry:
                response = reply
                break
        
        self.response_label.config(text=response)
        self.tree.insert("", tk.END, values=(inquiry, response))
        self.inquiry_entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = InquirySystem(root)
    root.mainloop()
