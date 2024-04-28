import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x200')
        self.bind('<Key>', self.on_key_press)

    def on_key_press(self, event):
        print(f'button activated: {event.char}')

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()
