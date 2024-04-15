import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes
from Gui.HomePage import Home_func
from Gui.Sidebar import SideBar_func


class Main(ctk.CTk):
    # Initial attributes
    def __init__(self):
        super().__init__()
        self.title('')
        self.geometry("1300x686+100+80")
        # self.geometry("900x700+400+70")
        # self.attributes("-fullscreen", True)
        self.bind('<Escape>', lambda event: self.quit())

        # Call the main screen
        Home_screen(self) 
        SideBar_func(self)

        # run
        self.mainloop()

        # Initial Animation

        # Home screen
class Home_screen():
    def __init__(self, parent):
        Home_func(parent)

class Sidebar_screen():
    def __init__(self, parent):
        SideBar_func(parent)

Main()
