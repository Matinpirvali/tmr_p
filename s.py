import tkinter as tk

def order_burger(burger_name):
    print(f"You ordered {burger_name} burger.")

root = tk.Tk()
root.title("Burger Menu")

# Create a frame to hold the burger menu
frame = tk.Frame(root)
frame.pack(pady=20)

# Burger options to display in the menu
burger_options = ["Classic Burger", "Cheeseburger", "Bacon Burger", "Veggie Burger"]

# Create a Menubutton for the burger menu
burger_menu = tk.Menubutton(frame, text="Select Burger", relief=tk.RAISED)
burger_menu.grid(row=0, column=0, padx=10, pady=5)
burger_menu.menu = tk.Menu(burger_menu, tearoff=0)

# Add burger options to the menu
for burger_name in burger_options:
    burger_menu.menu.add_command(label=burger_name, command=lambda name=burger_name: order_burger(name))

# Attach the menu to the Menubutton
burger_menu["menu"] = burger_menu.menu

root.mainloop()
