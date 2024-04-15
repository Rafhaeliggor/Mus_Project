import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes

class SideBar_func(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkFrame(parent, width=200, height= 200, fg_color="#464646", bg_color="#2F2F2F").place(relx = 0.81, rely= 0.025, relheight=0.95, relwidth=0.18, anchor='nw')
