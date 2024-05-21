import customtkinter as ctk
import pygame.midi

# inicialise pygame
pygame.midi.init()

# simple configuration
player = pygame.midi.Output(0)

# Notes liv
notes = {
    'C': 60,
    'D': 62,
    'E': 64,
    'F': 65,
    'G': 67,
    'A': 69,
    'B': 71
}

#sound output function
def play_note(note):
    player.note_on(notes[note], 127)  #127 = velocity
    app.after(500, lambda: player.note_off(notes[note], 127))  # stops the note after 500ms


app = ctk.CTk()  # Cria a janela principal
app.geometry("300x400")
app.title("Piano MIDI")

#buttons for each note
buttons = {}
for note in notes:
    button = ctk.CTkButton(app, text=note, command=lambda n=note: play_note(n))
    button.pack(pady=10)
    buttons[note] = button

app.mainloop()

#finish pygame
pygame.midi.quit()
