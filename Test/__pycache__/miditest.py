import customtkinter as ctk
import pygame.midi

# Inicializa o pygame.midi
pygame.midi.init()

# Configura o dispositivo de saída MIDI
player = pygame.midi.Output(0)

# Notas MIDI
notes = {
    'C': 60,
    'D': 62,
    'E': 64,
    'F': 65,
    'G': 67,
    'A': 69,
    'B': 71
}

# Função para reproduzir o som da nota
def play_note(note):
    player.note_on(notes[note], 127)  # Inicia a nota com velocidade 127 (máxima)
    app.after(500, lambda: player.note_off(notes[note], 127))  # Para a nota após 500ms

# Configura o CustomTkinter
ctk.set_appearance_mode("dark")  # Modo de aparência
ctk.set_default_color_theme("blue")  # Tema de cor

app = ctk.CTk()  # Cria a janela principal
app.geometry("300x400")
app.title("Piano MIDI")

# Cria botões para cada nota
buttons = {}
for note in notes:
    button = ctk.CTkButton(app, text=note, command=lambda n=note: play_note(n))
    button.pack(pady=10)
    buttons[note] = button

app.mainloop()

# Finaliza o pygame.midi
pygame.midi.quit()
