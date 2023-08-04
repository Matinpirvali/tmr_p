import tkinter as tk
import customtkinter as ctk
from PIL import Image
import os

# Places ANCHOR
class place:
    # up
    up = "n"
    up_right = "ne"
    up_left = "nw"

    # left
    left_up = "wn"
    left_down = "ws"
    left = "w"

    # right
    right = "e"
    right_down = "es"
    right_up = "en"

    # down
    down = "s"
    down_right = "se"
    down_right = "sw"


# Page one CHATBOT
class PageOne_BOT(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        

        # Full Screen Code
        pad=1
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>',self.toggle_geom)

        # Objects

        label = ctk.CTkLabel(self, text="The is Page one")
        label.pack(pady=10, padx=10)

        button = ctk.CTkButton(self, text="Go Page Two", command=lambda: controller.show_frame(PageTwo_VIDEO))
        button.pack(anchor=place.up_right) # anchor="ne"

    # Full Screen function
    def toggle_geom(self,event):
        geom=self.controller.winfo_geometry()
        print(geom,self._geom)
        self.controller.geometry(self._geom)
        self._geom=geom


# Page two SHARE_VIDEO
class PageTwo_VIDEO(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.new_frame_status = False

        # Full Screen Code
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>',self.toggle_geom)

        # image & icons
        burger_icon = ctk.CTkImage(light_image=Image.open("./assets/icons/burger_icon.png"),
                                  size=(32, 32))
        
        # Objects

        # Freame Header Row
        Header_Row_freame = ctk.CTkFrame(self)
        Header_Row_freame.pack(pady=10, padx=10 ,anchor=place.up, fill='x')

        button_burger_menu = ctk.CTkButton(Header_Row_freame, text="", image=burger_icon, width=60)
        button_burger_menu.pack(pady=5, padx=10, anchor=place.up_right)
        button_burger_menu.configure(command=self.on_burger_menu_click)

        # ---
        search_entry = ctk.CTkEntry(Header_Row_freame, placeholder_text="Search", font=('Roboto', 20), corner_radius=200, width=1000)
        search_entry.pack(pady=5,anchor=place.up)

    def on_burger_menu_click(self):
        if not self.new_frame_status:
            self.create_frame()
            self.new_frame_status = True
        
    def create_frame(self):
        setting_frame = ctk.CTkFrame(self, height=900)
        setting_frame.pack(pady=5, padx=10, anchor=place.right, fill='y')

        button_bot_page = ctk.CTkButton(setting_frame, text="Chat Bot", font=('bold', 13), width=100,command=lambda: self.show_frame(PageOne_BOT))
        button_bot_page.pack(pady=5, padx=10 ,anchor=place.up_right)

        button_profile_page = ctk.CTkButton(setting_frame, text="Profile", font=('bold', 13), width=100)
        button_profile_page.pack(pady=5, padx=10 ,anchor=place.up_right)

        button_exit_page = ctk.CTkButton(setting_frame, text="Exit", font=('bold', 13),fg_color='#B80F0A', hover_color='#7C0A02' ,command=self.exit, width=100)
        button_exit_page.pack(pady=5, padx=10 ,anchor=place.up_right) 
        
    def show_frame(self, cont):
        frame = self.controller.frames[cont]
        frame.tkraise()

    def exit(self):
        exit()

    
    # Full Screen function
    def toggle_geom(self, event):
        geom=self.controller.winfo_geometry()
        print(geom,self._geom)
        self.controller.geometry(self._geom)
        self._geom=geom


# MAIN 
class MAIN(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title('TMR_P')

        self.frames = {}
        
        for F in (PageTwo_VIDEO, PageOne_BOT):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(PageTwo_VIDEO)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = MAIN()
    app.mainloop()