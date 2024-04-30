import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x200')
        self.bind('<Key>', self.on_key_press)
        self.test_instance = Test()

    def on_key_press(self, event):
        Test.call_the_other(char = event.char)

    def run(self):
        self.mainloop()


class Test():
    def __init__(self):
        print('ok')

    def call_the_other(self, char):
        print(f'button activated: {char}')

app = MyApp()
app.run()
