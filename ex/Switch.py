import customtkinter
import tkinter

root = customtkinter.CTk()

switch_var = customtkinter.StringVar(value="on")

def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_1 = customtkinter.CTkSwitch(master=root, text="CTkSwitch", command=switch_event,
                                   variable=switch_var, onvalue="on", offvalue="off")
switch_1.pack(padx=20, pady=10)

root.mainloop()