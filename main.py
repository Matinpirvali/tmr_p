import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import platform 

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

    center = 'center'


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











# BOOOOOOOOOOOOOOOOOOOOOOOOOOT










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
        self.burger_icon = ctk.CTkImage(light_image=Image.open("./assets/icons/burger_icon.png"),
                                  size=(32, 32))
        
        # Objects

        # Freame Header Row
        self.Header_Row_freame = ctk.CTkFrame(self)
        self.Header_Row_freame.pack(pady=10, padx=10 ,side='top', fill='x', expand=False)

        button_burger_menu = ctk.CTkButton(self.Header_Row_freame, text="", image=self.burger_icon, width=60)
        button_burger_menu.pack(pady=5, padx=10, anchor=place.right)
        button_burger_menu.configure(command=self.on_burger_menu_click)

        # ---

        self.search_entry = ctk.CTkEntry(self.Header_Row_freame, placeholder_text="Search keyword", font=('Roboto', 20), corner_radius=200, width=1000)
        self.search_entry.pack(pady=15, padx=20)
        self.search_entry.bind("<Return>", self.search_videos)
        self.search_entry.bind("<KP_Enter>", self.search_videos)

        # self.videos_frame = ctk.CTkFrame(self, width=1100)
        # self.videos_frame.pack(pady=5, padx=10, side='left', fill='y', expand=False)

        self.video_buttons = []
        self.video_list = [
                    "Video 1",
                    "Video 2",
                    "Video 3",
                    "Video 4"]
        
        self.video_thumbnails = {
            "Video 1": "video1_image.png",
            "Video 2": "video2_image.jpg",
            "Video 3": "video3_image.jpg",
            "Video 4": "video4_image.jpg"
            # Add more thumbnails for other videos as needed
        }

    def delet_burger_menu_click(self):
        self.setting_frame.destroy()
    
    def on_burger_menu_click(self):
        print(self.new_frame_status)
        if self.new_frame_status == False:
            self.create_frame()
            self.new_frame_status = True
            print(self.new_frame_status)
        else:
            self.delet_burger_menu_click()
            self.new_frame_status = False
            print(self.new_frame_status)
    
    def create_frame(self):
        self.setting_frame = ctk.CTkFrame(self, height=900)
        self.setting_frame.pack(pady=5, padx=10, side='right', fill='y', expand=False)

        self.button_bot_page = ctk.CTkButton(self.setting_frame, text="Chat Bot", font=('bold', 13), width=145,command=lambda: self.show_frame(PageOne_BOT))
        self.button_bot_page.pack(pady=5, padx=10)

        self.button_profile_page = ctk.CTkButton(self.setting_frame, text="Profile", font=('bold', 13), width=145)
        self.button_profile_page.pack(pady=5, padx=10)

        self.optionmenu_var = ctk.StringVar(value="List of study fields")  # set initial value
        self.combobox = ctk.CTkOptionMenu(master=self.setting_frame,
                                    values=["Mathematical Physics", "Agricultural engineering and natural resources", "Humanities", "Medical sciences", "language and literature", "Art", "Geology", "biology", "chemistry", "physics", "Mathematics", "computer science"],
                                    command=self.optionmenu_callback,
                                    variable=self.optionmenu_var)
        self.combobox.pack(padx=20, pady=10)

        self.button_exit_page = ctk.CTkButton(self.setting_frame, text="Exit", font=('bold', 13),fg_color='#B80F0A', hover_color='#7C0A02' ,command=self.exit, width=145)
        self.button_exit_page.pack(pady=5, padx=10) 
        
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
    
    def play_video(self, video):
        print(f"Playing video: {video}")
    
    # Search funs
    def search_videos(self, event):
        keyword = self.search_entry.get()
        # Delete Previous Buttons
        for button in self.video_buttons:
            button.destroy()
        
        for video in self.video_list:
            if keyword.lower() in video.lower():
                thumbnail_filename = self.video_thumbnails.get(video, "default_thumbnail.png")  # Use a default thumbnail if not found
                thumbnail_path = f"./assets/thumbnails/{thumbnail_filename}"  # Assuming your thumbnail images are in a folder named "thumbnails"
                
                thumbnail_image = Image.open(thumbnail_path)
                thumbnail_image = thumbnail_image.resize((200, 200), Image.ANTIALIAS)
                thumbnail_tk = ImageTk.PhotoImage(thumbnail_image)
                
                video_button = ctk.CTkButton(self, text=video, image=thumbnail_tk, compound="top", command=lambda v=video: self.play_video(v))
                video_button.thumbnail_tk = thumbnail_tk  # Store a reference to avoid garbage collection
                video_button.pack(pady=5, padx=10, expand=True, side='left')
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

        scrollbar = ctk.CTkScrollbar(self)
        value_1, value_2 = scrollbar.get()
        scrollbar.set(value_1, value_2)

        # icon
        p1 = tk.PhotoImage(file="./icon.png")
        self.iconphoto(False, p1)

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
    operating_system=platform.system()
    app = MAIN()
    app.mainloop()
