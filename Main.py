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
        self.Home_screen_var = Home_screen(self)

        self.bind('<Key>', self.on_key_press)

    def on_key_press(self, event):
        self.Home_screen_var.call_the_other(event.char)


        # run
    def run_window(self):
        self.mainloop()


        # Initial Animation

        # Home screen
class Home_screen():
    def __init__(self, parent):
        self.screen_Home = Gui.Screen(parent) 
        self.screen_Home.sidebar()
        self.screen_Home.mode_1_screen()

    def call_the_other(self, char):
        self.screen_Home.get_answer_note(char)

App = Main()
App.run_window()
