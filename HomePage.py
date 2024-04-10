import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes

class Home_func(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        def task_button(master):
            botao_teste = ctk.CTkButton(master, fg_color="black", width=100, height=20, text='teste', command = lambda: print('Teste'))
            botao_teste.pack(navegator)
            print('entrou no task button')

        print('chegou na função')
        navegator = ctk.CTkFrame(parent, fg_color='white')
        esfera = ctk.CTkCanvas(navegator, width=200, height= 200)
        esfera.create_aa_circle(fill='blue',x_pos=100,y_pos=100,radius=95)
        esfera.pack(pady=10)
        print('Antes do teskbutton')
        task_button(navegator)

        #Puting the navegator barr
        navegator.place(relx = 0.81, rely= 0.025, relheight=0.95, relwidth=0.18, anchor='nw')
