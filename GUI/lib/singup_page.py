import customtkinter as ctk
import tkinter.messagebox as tkmb


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Login Page")


def login():
	users = []
	passwords = []
	
	new_window = ctk.CTkToplevel(app)

	new_window.title("New Window")

	new_window.geometry("350x150")


	if len(user_entry.get()) <= 8 and user_pass.get() == user_pass_com.get():
		un = user_entry.get()
		pw = user_pass.get()
		
        # Append un & pw to users & passwords LIST and upgrade system to DATABASE ;) ...dadmehr...
		
		tkmb.showinfo(title="Singup Successful",message="You have Singed in Successfully")
		ctk.CTkLabel(new_window,text="Welcome User").pack()
	elif len(user_entry.get()) > 8 :
		tkmb.showinfo(title="Sing up Failed",message="Username should be more than 8 digits")
	elif len(user_pass.get()) > 8 :
		tkmb.showinfo(title="Sing up Failed",message="Password should be more than 8 digits")
	else:
		tkmb.showerror(title="Sing up Failed",message="Invalid Username and password")



label = ctk.CTkLabel(app,text="Sing up")

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label.pack(pady=12,padx=10)


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

user_pass_com= ctk.CTkEntry(master=frame,placeholder_text="Again Password",show="*")
user_pass_com.pack(pady=12,padx=10)


button = ctk.CTkButton(master=frame,text='Singup',command=login)
button.pack(pady=12,padx=10)


app.mainloop()
