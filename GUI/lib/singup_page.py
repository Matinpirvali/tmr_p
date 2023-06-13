from customtkinter import *

def signup():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if username and password and confirm_password:
        if password == confirm_password:
            print("Signup Successful", "Account created successfully!")
            # Add your code to proceed to the next steps or login page
        else:
            print("Signup Failed", "Password and confirm password must match!")
            password_entry.delete(0, CTk.END)
            confirm_password_entry.delete(0, CTk.END)
    else:
        print("Signup Failed", "Please fill in all the fields!")

# Create the main window
root = CTk()
root.title("Signup Page")
root.geometry("300x250")

# Create a frame
frame = CTkFrame(root)
frame.pack(pady=20)

# Create labels
username_label = CTkLabel(frame, text="Username ")
username_label.grid(row=0, column=0)
password_label = CTkLabel(frame, text="Password ")
password_label.grid(row=1, column=0)
confirm_password_label = CTkLabel(frame, text="Confirm Password ")
confirm_password_label.grid(row=2, column=0)

# Create entry fields
username_entry = CTkEntry(frame)
username_entry.grid(row=0, column=1)
password_entry = CTkEntry(frame, show="*")
password_entry.grid(row=1, column=1)
confirm_password_entry = CTkEntry(frame, show="*")
confirm_password_entry.grid(row=2, column=1)

# Create a signup button
signup_button = CTkButton(root, text="Sign Up", command=signup)
signup_button.pack()

root.mainloop()
