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
            #Create size and position customizabable
            print("entrou na função")
            screenTest.create_oval((110, 450, 250, 350), fill="black")
            screenTest.create_rectangle((250,150, 235, 400), fill="black")
            
        #Canvas
        
        screenTest = ctk.CTkCanvas(self, width=100, height=100)
        #screenTest.create_aa_circle(x_pos=50, y_pos=50, radius=10, fill = "black", angle=180)
        create_oval_test()
        screenTest.pack(expand=True, fill='both')

        self.mainloop()

App()