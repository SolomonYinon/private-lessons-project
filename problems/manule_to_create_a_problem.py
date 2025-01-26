import tkinter as tk
from tkinter import ttk

class HelpWindow:
    def __init__(self, master):
        self.master = master
        master.title("How to Submit a New Problem")
        master.geometry("600x400")

        ttk.Label(master, text="How to Submit a Problem", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Create a frame for scrolling text
        frame = ttk.Frame(master)
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Add a scrollable text widget
        text_widget = tk.Text(frame, wrap="word", height=10, width=70, font=("Helvetica", 12))
        text_widget.pack(side="left", fill="both", expand=True)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(frame, command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scrollbar.set)

        # Instructions content
        instructions = """\
To submit a new problem, follow these steps:

1. Open the 'Submit a Problem' page.
2. Type a clear description of the issue in the text box.
3. Click the 'Submit' button.
4. You will see a confirmation message if the submission is successful.
5. Your problem is now saved and can be reviewed by an admin.

Note:
- Be as detailed as possible when describing the issue.
- If you encounter an error, ensure the data file is accessible.

For further help, contact support.
"""

        # Insert text and disable editing
        text_widget.insert("1.0", instructions)
        text_widget.config(state="disabled")

        # Back button
        ttk.Button(master, text="Back", command=master.destroy).pack(pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    app = HelpWindow(root)
    root.mainloop()
