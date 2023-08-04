import customtkinter

class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="RadioButtonFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Option 1", value="Option 1", variable=self.radio_button_var)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Option 2", value="Option 2", variable=self.radio_button_var)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)
        self.radio_button_3 = customtkinter.CTkRadioButton(self, text="Option 3", value="Option 3", variable=self.radio_button_var)
        self.radio_button_3.grid(row=3, column=0, padx=10, pady=(10, 20))

    def get_value(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        return self.radio_button_var.get()

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)
        
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("RadioButtonFrame test")

        self.radio_button_frame_1 = RadioButtonFrame(self, header_name="RadioButtonFrame 1")
        self.radio_button_frame_1.grid(row=0, column=0, padx=20, pady=20)

        self.frame_1_button = customtkinter.CTkButton(self, text="Print value of frame 1", command=self.print_value_frame_1)
        self.frame_1_button.grid(row=1, column=0, padx=20, pady=10)

    def print_value_frame_1(self):
        print(f"Frame 1 value: {self.radio_button_frame_1.get_value()}")


if __name__ == "__main__":
    app = App()
    app.mainloop()