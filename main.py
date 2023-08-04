import tkinter as tk
import customtkinter as ctk


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

        # Full Screen Code
        pad=3
        self._geom='500x600+0+0'
        controller.geometry("{0}x{1}+0+0".format(
            controller.winfo_screenwidth()-pad, controller.winfo_screenheight()-pad))
        controller.bind('<F11>',self.toggle_geom)

        # Objects

        # label = ctk.CTkLabel(self, text="The is Page Two")
        # label.pack(pady=10, padx=10)
        
        button = ctk.CTkButton(self, text="Chat Bot",font=('bold', 15) ,command=lambda: controller.show_frame(PageOne_BOT))
        button.pack()
    
    # Full Screen function
    def toggle_geom(self,event):
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