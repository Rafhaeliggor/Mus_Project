import tkinter as tk

class CountdownApp:
    def __init__(self, master, countdown_duration):
        self.master = master
        self.master.title("Regressive time")

        self.countdown_duration = countdown_duration
        self.remaining_time = self.countdown_duration

        self.countdown_label = tk.Label(master, text=str(self.remaining_time), font=('Arial', 24))
        self.countdown_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_countdown)
        self.start_button.pack()

    def start_countdown(self):
        self.start_button.config(state=tk.DISABLED)
        self.countdown()

    def countdown(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_countdown_label()
            self.master.after(1000, self.countdown)
        else:
            self.countdown_label.config(text="Time out!")

    def update_countdown_label(self):
        self.countdown_label.config(text=str(self.remaining_time))

def main():
    countdown_duration = 10 
    root = tk.Tk()
    app = CountdownApp(root, countdown_duration)
    root.mainloop()

if __name__ == "__main__":
    main()
