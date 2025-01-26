import tkinter as tk
from tkinter import ttk, messagebox
import json

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            # Ensure "problems" key exists
            if "problems" not in data:
                data["problems"] = []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"problems": []}  # Handle empty or corrupted JSON


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

class ProblemSubmission:
    def __init__(self, master):
        self.master = master
        master.title("Submit a New Problem")
        master.geometry('600x400')

        ttk.Label(master, text="Describe the Problem:", font=("Helvetica", 14)).pack(pady=10)
        self.problem_entry = tk.Text(master, height=5, width=60)
        self.problem_entry.pack(pady=5)

        ttk.Button(master, text="Submit", command=self.submit_problem).pack(pady=10)
    
    def submit_problem(self):
        problem_text = self.problem_entry.get("1.0", tk.END).strip()
        if not problem_text:
            messagebox.showwarning("Warning", "Problem description cannot be empty!")
            return
        
        data = load_data()
        data["problems"].append({"description": problem_text})
        save_data(data)
        
        messagebox.showinfo("Success", "Problem submitted successfully!")
        self.problem_entry.delete("1.0", tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = ProblemSubmission(root)
    root.mainloop()
