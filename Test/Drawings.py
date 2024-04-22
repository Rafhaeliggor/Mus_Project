import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Drawing")
        self.geometry("400x400")
        self.bind("<Escape>", lambda event: self.quit())
                
        def create_oval_test():
            #x_oval = 140, y_oval = 100, x_line = 15, y_line = 250

            #custom zx,zy = center of oval
            #oval ((x1,y1, x2, y2) -> ((zx-70, zy-50, zx+70, zy+50))
            #line ((zx+15,zy+250,zx+70,zy))

            #Create size and position customizabable
            zx = 200
            zy = 300
            t = 1

            screenTest.create_oval((zx-7*t, zy-5*t, zx+7*t, zy+5*t), fill="black")
            screenTest.create_rectangle((zx+5*t,zy-25*t,zx+7*t,zy), fill="black")
            #screenTest.create_aa_circle(x_pos=zx, y_pos=zy, radius=3, fill="red")

            #screenTest.create_oval((110, 450, 250, 350), fill="black")
            #screenTest.create_rectangle((250,150, 235, 400), fill="black")
            
        #Canvas
        
        screenTest = ctk.CTkCanvas(self, width=100, height=100)
        #screenTest.create_aa_circle(x_pos=50, y_pos=50, radius=10, fill = "black", angle=180)
        create_oval_test()
        screenTest.pack(expand=True, fill='both')

        self.mainloop()

App()