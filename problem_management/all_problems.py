import tkinter as tk
from tkinter import ttk, messagebox
import json

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"problems": []}

class AdminProblemViewer:
    def __init__(self, master):
        self.master = master
        master.title("View Submitted Problems")
        master.geometry('700x500')

        ttk.Label(master, text="Submitted Problems:", font=("Helvetica", 14)).pack(pady=10)
        
        self.tree = ttk.Treeview(master, columns=("#1"), show='headings')
        self.tree.heading("#1", text="Problem Description")
        self.tree.column("#1", width=650)
        self.tree.pack(pady=5, fill=tk.BOTH, expand=True)
        
        ttk.Button(master, text="Refresh", command=self.load_problems).pack(pady=10)
        self.load_problems()

    def load_problems(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        data = load_data()
        for problem in data.get("problems", []):
            self.tree.insert("", tk.END, values=(problem["description"],))

if __name__ == '__main__':
    root = tk.Tk()
    app = AdminProblemViewer(root)
    root.mainloop()
