import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes

class Screen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        ctk.CTkFrame(parent, fg_color='#2F2F2F', bg_color='#2F2F2F').pack(fill="both", expand=True)

    def sidebar(self):
        sidebar_var = ctk.CTkFrame(self.parent, width=200, height= 200, fg_color="#464646", bg_color="#2F2F2F")
        sidebar_var.place(relx = 0.81, rely= 0.025, relheight=0.95, relwidth=0.18, anchor='nw')

        esfera = ctk.CTkCanvas(master=sidebar_var, width=200, height= 200, bg="#464646", highlightbackground="#464646", highlightcolor="#464646")
        esfera.create_aa_circle(fill='#D9D9D9',x_pos=100,y_pos=100,radius=95)
        esfera.pack(pady=15)

        for c in range (0,5):
            botao_teste = ctk.CTkButton(sidebar_var,hover_color="#A0A0A0", fg_color="#D9D9D9", width=200, height=70, text='teste', command = self.destroy_msg, text_color="#454545")
            botao_teste.pack(pady= 4)

        ctk.CTkButton(sidebar_var, hover_color="#A0A0A0" ,text="Sair", height=100, width=100, fg_color='#D9D9D9', text_color="#454545", command= lambda: self.quit()).place(relx= 0.7, rely=0.9, relwidth=0.25, relheight=0.09, anchor='nw')
    
    def welcome_msg(self):
        self.msg_frame = ctk.CTkFrame(self.parent, fg_color='#2F2F2F', bg_color='#2F2F2F')
        self.msg_frame.place(relx = 0, rely =0, relheight=1, relwidth=0.8)

        ctk.CTkLabel(self.msg_frame, text="WELCOME", font=('Roboto', 80, 'bold'), text_color="#454545", bg_color="#2F2F2F").place(relx=0.5, rely= 0.4, anchor='center')
        ctk.CTkLabel(self.msg_frame, text="SELECT AN TASK", font=('Roboto', 30, 'bold'), text_color="#454545", bg_color="#2F2F2F").place(relx=0.5, rely=0.475, anchor='center')

        
    def destroy_msg(self):
        self.msg_frame.destroy()
        self.settings_screen()

    def settings_screen(self):
        self.settings_frame = ctk.CTkFrame(self.parent, bg_color='red', fg_color='red')
        self.settings_frame.place(relx = 0, rely =0, relheight=1, relwidth=0.8)

class Home_func(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.base(parent)

    def base(self, parent):
        self.base = ctk.CTkFrame(parent, bg_color="#2F2F2F", fg_color="#2F2F2F")
        self.base.pack(fill="both", expand=True)
        self.welcome_msg = ctk.CTkFrame(parent, bg_color="#2F2F2F", fg_color="#2F2F2F")
        self.welcome_settings()
        self.place_txt()
        
    def place_txt(self):
        self.welcome_msg.place(relx= 0.405, rely= 0.4, anchor='center')
        #self.destroy_txt()

    def destroy_txt(self):
        print('ok')
        self.welcome_msg.destroy()
        

    def welcome_settings(self):
        ctk.CTkLabel(self.welcome_msg, text="WELCOME", font=('Roboto', 80, 'bold'), text_color="#454545", bg_color="#2F2F2F").pack()
        ctk.CTkLabel(self.welcome_msg, text="SELECT AN TASK", font=('Roboto', 30, 'bold'), text_color="#454545", bg_color="#2F2F2F").pack()

        
