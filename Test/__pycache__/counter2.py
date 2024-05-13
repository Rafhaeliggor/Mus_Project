import tkinter as tk
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')
        self.title('Test')
        self.text_var = ctk.CTkLabel(self, text='Started')
        self.text_var.pack()
        self.counter(10)

    def counter(self, seconds):
        if seconds >= 0:
            self.text_var.configure(text= f'{seconds}')
            self.after(1000, lambda: self.counter(seconds - 1))
        else:
            self.text_var.configure(text='Fineshed')

    
        
time_duration = 20
root = App()
root.mainloop()
