import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes

class Home_func(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        def open_welcome(parent):
            welcome_msg = ctk.CTkFrame(parent, bg_color="#2F2F2F", fg_color="#2F2F2F")
            ctk.CTkLabel(welcome_msg, text="WELCOME", font=('Roboto', 80, 'bold'), text_color="#454545", bg_color="#2F2F2F").pack()
            ctk.CTkLabel(welcome_msg, text="SELECT AN TASK", font=('Roboto', 30, 'bold'), text_color="#454545", bg_color="#2F2F2F").pack()
            welcome_msg.place(relx= 0.405, rely= 0.4, anchor='center')
            
        ctk.CTkFrame(parent, bg_color="#2F2F2F", fg_color="#2F2F2F").pack(fill="both", expand=True)

        open_welcome(parent)
