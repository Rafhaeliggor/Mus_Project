import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes
import Gui


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

        # run
        self.mainloop()

        # Initial Animation

        # Home screen
class Home_screen():
    def __init__(self, parent):
        screen_Home = Gui.Screen(parent)  # Criar uma instância de Screen
        screen_Home.sidebar()
        screen_Home.mode_1_screen()

Main()
