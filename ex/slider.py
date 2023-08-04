import customtkinter
import tkinter

root = customtkinter.CTk()

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(master=root, from_=0, to=100, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()