import tkinter as tk
from tkinter import ttk

class LessonOrganizationInterface:
    def __init__(self, master):
        self.master = master
        master.title("Lesson Organization")
        master.geometry('400x300')  # Set window size

        # Create a frame for better organization
        frame = ttk.Frame(master, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        title_label = ttk.Label(frame, text="Organize Lessons", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Organize Lessons Button
        self.submit_button = ttk.Button(frame, text="Organize Lessons", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        # Logic to organize lessons
        print("Lessons organized!")

if __name__ == '__main__':
    from lesson_scheduling_logic import schedule_lessons
    root = tk.Tk()
    organization = LessonOrganizationInterface(root)
    root.mainloop()
