import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="The is Page one")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Go Page Two", command=lambda: controller.show_frame(PageTwo))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="The is Page Two")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Go Page one", command=lambda: controller.show_frame(PageOne))
        button.pack()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(PageOne)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()