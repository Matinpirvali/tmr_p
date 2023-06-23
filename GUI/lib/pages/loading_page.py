import tkinter as tk
from tkinter import ttk

def loading_page():
    root = tk.Tk()
    root.title("Loading Page")
    root.geometry("300x200")
    root.resizable(False, False)

    # Create a label for the loading message
    loading_label = ttk.Label(root, text="Loading...", font=("Arial", 14))
    loading_label.pack(pady=50)

    # Create a progress bar
    progress_bar = ttk.Progressbar(root, length=200, mode='indeterminate')
    progress_bar.pack()

    # Start the progress bar animation
    progress_bar.start(10)

    root.mainloop()

# Call the loading_page function to display the loading page
loading_page()

