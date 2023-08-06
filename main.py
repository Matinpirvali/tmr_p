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
    down_left = "sw"


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
        button_burger_menu.pack(pady=5, padx=10, anchor=place.right)
        button_burger_menu.configure(command=self.on_burger_menu_click)

        # ---

        search_entry = ctk.CTkEntry(Header_Row_freame, placeholder_text="Search keyword", font=('Roboto', 20), corner_radius=200, width=1000)
        search_entry.pack(pady=5, padx=2, )
        search_entry.bind("<Return>", self.search_videos)

        self.video_buttons = []
        self.video_list = [
                    "Video 1",
                    "Video 2",
                    "Video 3",
                    "Video 4"
                ]

    def on_burger_menu_click(self):
        if not self.new_frame_status:
            self.create_frame()
            self.new_frame_status = True
    
    def create_frame(self):
        setting_frame = ctk.CTkFrame(self, height=900)
        setting_frame.pack(pady=5, padx=10, anchor=place.right, fill='y')

        button_bot_page = ctk.CTkButton(setting_frame, text="Chat Bot", font=('bold', 13), width=145,command=lambda: self.show_frame(PageOne_BOT))
        button_bot_page.pack(pady=5, padx=10)

        button_profile_page = ctk.CTkButton(setting_frame, text="Profile", font=('bold', 13), width=145)
        button_profile_page.pack(pady=5, padx=10)

        optionmenu_var = ctk.StringVar(value="List of study fields")  # set initial value
        combobox = ctk.CTkOptionMenu(master=setting_frame,
                                       values=["Mathematical Physics", "Agricultural engineering and natural resources", "Humanities", "Medical sciences", "language and literature", "Art", "Geology", "biology", "chemistry", "physics", "Mathematics", "computer science"],
                                       command=self.optionmenu_callback,
                                       variable=optionmenu_var)
        combobox.pack(padx=20, pady=10)

        button_exit_page = ctk.CTkButton(setting_frame, text="Exit", font=('bold', 13),fg_color='#B80F0A', hover_color='#7C0A02' ,command=self.exit, width=145)
        button_exit_page.pack(pady=5, padx=10) 
        
    def show_frame(self, cont):
        frame = self.controller.frames[cont]
        frame.tkraise()

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)

    def exit(self):
        exit()
    
    # Full Screen function
    def toggle_geom(self, event):
        geom=self.controller.winfo_geometry()
        print(geom,self._geom)
        self.controller.geometry(self._geom)
        self._geom=geom


    # Search funs

    def play_video(self, video_name):
        # Video Player
        print(f"Playing Video: {video_name}")

    def search_videos(self):
        keyword = self.search_entry.get()

        # Delet Before Button
        for button in self.video_buttons:
            button.destroy()
        
        for video in self.video_list:
            if keyword.lower() in video.lower():
                # Create new Buttons for Videos
                video_button = ctk.CTkButton(self.root, text=video, command=lambda v=video: self.play_video(v))
                video_button.grid(row=self.video_list.index(video)+2, column=0, padx=10, pady=5)
                self.video_buttons.append(video_button)


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