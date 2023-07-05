import tkinter as tk

class ProfileDashboard:
    def __init__(self, name, age, email):
        self.window = tk.Tk()
        self.window.title("Profile Dashboard")
        
        self.name_label = tk.Label(self.window, text=f"Name: {name}")
        self.name_label.pack()

        self.age_label = tk.Label(self.window, text=f"Age: {age}")
        self.age_label.pack()

        self.email_label = tk.Label(self.window, text=f"Email: {email}")
        self.email_label.pack()

    def start(self):
        self.window.mainloop()

# Create an instance of the ProfileDashboard class and start the GUI
profile = ProfileDashboard("John Doe", 30, "johndoe@example.com")
profile.start()
