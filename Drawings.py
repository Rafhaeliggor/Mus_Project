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

        #Canvas
        
        screenTest = ctk.CTkCanvas(self, width=400, height=400)
        screenTest.create_line
        screenTest.create_aa_circle(x_pos=50, y_pos=50, radius=10, fill = "black", angle=180)
        screenTest.pack(expand=True, fill='both')
        
        def create_oval_test():
            shape =
        
        self.mainloop()

App()