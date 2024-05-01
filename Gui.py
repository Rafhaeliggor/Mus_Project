import tkinter as tk
import customtkinter as ctk
import json
from PIL import Image, ImageTk
from ctypes import windll, byref, sizeof, c_int
import ctypes
import logic

class Screen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        ctk.CTkFrame(parent, fg_color='#2F2F2F', bg_color='#2F2F2F').pack(fill="both", expand=True)

        #variables
        self.rounds_var = tk.IntVar()
        self.time_var = tk.IntVar()
        self.apbt_notation_var = tk.BooleanVar()
        self.solp_notation_var = tk.BooleanVar()
        self.extra_lines_var = tk.BooleanVar()
        self.f_key_var = tk.BooleanVar()

        self.points = 0

        self.keyboard_asw = ['a','s','d','h','j','k','l']

        #G_key_img
        p_img = Image.open("img/key_G_canvas.png")
        p_img_red = p_img.resize((155, 155), Image.ANTIALIAS)   
        self.key_p = ImageTk.PhotoImage(p_img_red)

        #F_key_img
        p2_img = Image.open("img/F_key_png.png")
        p2_img_red = p2_img.resize((61, 61), Image.ANTIALIAS)   
        self.key_f = ImageTk.PhotoImage(p2_img_red)

        g_img = Image.open("img/key_simbol.png")
        g_img.resize((50, 50))
        self.key_g = ImageTk.PhotoImage(g_img)

        
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
    
    def out_settings(self):
        print(f"Rounds: {self.rounds_var.get()}")
        print(f"Time: {self.time_var.get()}")
        print(f"Alphabet Notation: {self.apbt_notation_var.get()}")
        print(f"Extra lines: {self.extra_lines_var.get()}")
        print(f"F key active: {self.f_key_var.get()}")


    def alph_on(self):
        self.apbt_notation_var.set(True)
        self.solp_notation_var.set(False)
        print('alphabet on')
    
    def alph_off(self):
        self.apbt_notation_var.set(False)
        self.solp_notation_var.set(True)
        print('alpabet off')

    def create_canvas_base(self, parent):
        #pentagram
        self.notes_space = ctk.CTkCanvas(parent, height=200, width=400, bg='white', borderwidth=0, highlightthickness=0)
        for c in range(0,5):
            self.notes_space.create_rectangle((30,60+(c*20),365,60+(c*20)), fill="black")
    
        self.new_notes_key()

        self.note_draw(zx = 200, zy= 190, t = 2, note = self.note_list[0], rev= self.note_list[2])
        self.key_draw('g')

        self.extra_lines(0)
    
    def note_draw(self, zx, zy, t, note, rev = False):
        if rev == False:
            self.oval_note = self.notes_space.create_oval((zx-7*t, (zy-5*t)-note*10, zx+7*t, (zy+5*t)-note*10), fill="black")
            self.rectangle_note = self.notes_space.create_rectangle((zx+5*t,(zy-25*t)-note*10,zx+7*t,zy-note*10), fill="black")

        if rev == True:
            self.oval_note = self.notes_space.create_oval((zx-7*t, (zy-5*t)-note*10, zx+7*t, (zy+5*t)-note*10), fill="black")
            self.rectangle_note = self.notes_space.create_rectangle((zx+5*t,(zy+25*t)-note*10,zx+7*t,zy-note*10), fill="black")

    def extra_lines(self, amnt):
        self.extra1 = self.notes_space.create_rectangle((0, 1, 1, 0), fill="white")
        self.extra2 = self.notes_space.create_rectangle((0, 1, 1, 0), fill="white")
        self.extra3 = self.notes_space.create_rectangle((0, 1, 1, 0), fill="white")
        self.extra4 = self.notes_space.create_rectangle((0, 1, 1, 0), fill="white")

        if amnt == 0:
            print('')

        elif amnt == -1 or amnt == -2:
            self.extra1 = self.notes_space.create_rectangle((175,60+(5*20),225,60+(5*20)), fill="black")
            if amnt == -2:
                self.extra2 = self.notes_space.create_rectangle((175,60+(6*20),225,60+(6*20)), fill="black")

        elif amnt == 1 or 2:
            self.extra3 = self.notes_space.create_rectangle((175,20+(1*20),225,20+(1*20)), fill="black")
            if amnt == 2:
                self.extra4 = self.notes_space.create_rectangle((175,20+(0*20),225,20+(0*20)), fill="black")
        

    def key_draw(self, key):
        self.g_key_var = self.notes_space.create_rectangle((0, 1, 1, 0), fill="white")
        self.f_key_var = self.notes_space.create_rectangle((0, 1, 1, 0), fill="white")

        if key == 'g':
            self.g_key_var = self.notes_space.create_image(60,25, anchor='n', image= self.key_p)

        elif key == 'f':
            self.f_key_var = self.notes_space.create_image(60,61, anchor='n', image= self.key_f)

    def blank_canvas(self):
        self.notes_space.delete(self.extra1)
        self.notes_space.delete(self.extra2)
        self.notes_space.delete(self.extra3)
        self.notes_space.delete(self.extra4)    

        self.notes_space.delete(self.oval_note)
        self.notes_space.delete(self.rectangle_note)
        self.notes_space.delete(self.g_key_var)
        self.notes_space.delete(self.f_key_var)

        
    def get_answer_note(self, char):
        if char in self.keyboard_asw:
            verify = self.new_note.verify_note(asw=char, quest= self.note_list[0])

            if verify == True:
                self.add_points()
            elif verify == False:
                print('Wrong')
            self.reset_canvas()

    def new_notes_key(self):
        self.new_note = logic.notes_system()
        self.note_list = self.new_note.random_note()

    def reset_canvas(self):
        self.new_notes_key()

        self.blank_canvas()
        self.key_draw('g')
        
        self.extra_lines(self.note_list[1])

        self.note_draw(zx = 200, zy= 190, t = 2, note = self.note_list[0], rev= self.note_list[2])
    
    def add_points(self):
        self.points += 1
        self.points_var_label.configure(text=f'Points: {self.points}')


    def settings_screen(self):
        self.settings_frame = ctk.CTkFrame(self.parent, bg_color='#2F2F2F', fg_color='#2F2F2F')

        #Canvas
    
        #Pentagram
        for c in range(0,5):
            self.notes_space.create_rectangle((30,60+(c*20),365,60+(c*20)), fill="black")

        #Key
        self.notes_space.create_image(60,25, anchor='n', image= self.key_p)

        #Note
        zx = 200
        zy = 120
        t = 2
        
        self.notes_space.create_oval((zx-7*t, zy-5*t, zx+7*t, zy+5*t), fill="black")
        self.notes_space.create_rectangle((zx+5*t,zy-25*t,zx+7*t,zy), fill="black")
        
        self.notes_space.place(relx=0.5, rely=0.2, anchor='center')

        #"Rounds"
        ctk.CTkLabel(self.settings_frame, text='Rounds', font=('Roboto', 30, 'bold'), bg_color='transparent').place(relx=0.03, rely=0.32, relwidth=0.25, relheight=0.12, anchor='nw')
        ctk.CTkEntry(self.settings_frame, bg_color='#2F2F2F', font=('Roboto', 40, 'bold'), textvariable=self.rounds_var).place(relx=0.10, rely=0.40, relwidth=0.25, relheight=0.12)


        #"Time"
        ctk.CTkLabel(self.settings_frame, text='Time', font=('Roboto', 30, 'bold'), bg_color='transparent').place(relx=0.01, rely=0.54, relwidth=0.25, relheight=0.12, anchor='nw')
        ctk.CTkEntry(self.settings_frame, bg_color='#2F2F2F', font=('Roboto', 40, 'bold'), textvariable=self.time_var).place(relx=0.10, rely=0.62, relwidth=0.25, relheight=0.12)

        #Reading type
        self.key_alph_button = ctk.CTkButton(self.settings_frame, bg_color='#2F2F2F', fg_color='#464646', image= self.key_g, text='', command=self.alph_off).place(relx=0.12, rely=0.79, relwidth=0.08, relheight=0.12, anchor='nw')
        self.key_solp_button = ctk.CTkButton(self.settings_frame, bg_color='#2F2F2F',  fg_color='#464646', text='G', font=('Roboto', 60, 'bold'), command=self.alph_on).place(relx=0.25, rely=0.79, relwidth=0.08, relheight=0.12, anchor='nw')
        
        #Extras lines
        ctk.CTkLabel(self.settings_frame, text='Extras lines', bg_color='transparent', fg_color='transparent', font=('Roboto', 30, 'bold')).place(relx=0.55, rely=0.32, relwidth=0.25, relheight=0.12, anchor='nw')
        ctk.CTkSwitch(self.settings_frame,text='', corner_radius=5.5, switch_height=83, switch_width=180, button_length=70, variable=self.extra_lines_var).place(relx=0.60, rely=0.40, relwidth=0.25, relheight=0.12, anchor='nw')

        #F key
        ctk.CTkLabel(self.settings_frame, text='F KEY', bg_color='transparent', fg_color='transparent', font=('Roboto', 30, 'bold')).place(relx=0.52, rely=0.545, relwidth=0.25, relheight=0.12, anchor='nw')
        ctk.CTkSwitch(self.settings_frame,text='', corner_radius=5.5, switch_height=83, switch_width=180, button_length=70, variable=self.f_key_var).place(relx=0.60, rely=0.625, relwidth=0.25, relheight=0.12, anchor='nw')

        #Start
        ctk.CTkButton(self.settings_frame, bg_color='#2F2F2F',  fg_color='#464646', font=('Roboto', 50, 'bold'), text= 'Start', command=self.var_screen).place(relx=0.70, rely=0.79, relwidth=0.20, relheight=0.12, anchor='nw')

        self.settings_frame.place(relx = 0, rely =0, relheight=1, relwidth=0.8)

    def destroy_settings(self):
        self.settings_frame.destroy()

    def var_screen(self):
        self.destroy_settings()
        self.var_frame = ctk.CTkFrame(self.parent)

        ctk.CTkLabel(self.var_frame, text=(f"Rounds: {self.rounds_var.get()}")).pack()
        ctk.CTkLabel(self.var_frame, text=(f"Time: {self.time_var.get()}")).pack()
        ctk.CTkLabel(self.var_frame, text=(f"Alphabet notation: {self.apbt_notation_var.get()}")).pack()
        ctk.CTkLabel(self.var_frame, text=(f"Extra lines: {self.extra_lines_var.get()}")).pack()
        ctk.CTkLabel(self.var_frame, text=(f"F key: {self.f_key_var.get()}")).pack()

        self.var_frame.place(relx = 0, rely =0, relheight=1, relwidth=0.8)
    

    #def pentagram_draw(self, parent):

    #def gey_g_draw(self, parent):


    def mode_1_screen(self):
        self.mode1_frame = ctk.CTkFrame(self.parent, bg_color='#2F2F2F', fg_color='#2F2F2F')

        #Canvas
        self.create_canvas_base(self.mode1_frame)

        #Key

        #Note
        zx = 200
        zy = 120
        t = 2

        self.notes_space.place(relx=0.5, rely=0.2, anchor='center')

        ctk.CTkLabel(self.mode1_frame, text='X / Y', font=('Roboto', 30, 'bold'), text_color="#D9D9D9").place(anchor='w', rely=0.05, relx= 0.90)
        self.points_var_label = ctk.CTkLabel(self.mode1_frame, text= f'Points: {self.points}', font=('Roboto', 30, 'bold'), text_color="#D9D9D9")
        self.points_var_label.place(anchor='w', rely=0.05, relx= 0.05)

        c_button = ctk.CTkButton(self.mode1_frame, text='C', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('a')).place(relx=0.11, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')
        d_button = ctk.CTkButton(self.mode1_frame, text='D', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('s')).place(relx=0.21, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')
        e_button = ctk.CTkButton(self.mode1_frame, text='E', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('d')).place(relx=0.31, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')
        f_button = ctk.CTkButton(self.mode1_frame, text='F', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('h')).place(relx=0.51, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')
        g_button = ctk.CTkButton(self.mode1_frame, text='G', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('j')).place(relx=0.61, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')
        a_button = ctk.CTkButton(self.mode1_frame, text='A', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('k')).place(relx=0.71, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')
        b_button = ctk.CTkButton(self.mode1_frame, text='B', bg_color='transparent', fg_color="#D9D9D9", font=('Roboto', 30, 'bold'),hover_color="#A0A0A0", text_color='#2F2F2F', command= lambda: self.get_answer_note('l')).place(relx=0.81, rely=0.50, relwidth=0.08, relheight=0.12, anchor='nw')


        exit_button = ctk.CTkButton(self.mode1_frame, bg_color='transparent', fg_color='#464646', text='EXIT', command= lambda: print("Exit")).place(relx=0.02, rely=0.85, relwidth=0.08, relheight=0.12, anchor='nw')
        self.mode1_frame.place(relx = 0, rely =0, relheight=1, relwidth=0.8)

    
