import random
import tkinter as tk
from tkinter import messagebox

def sortear_ganadores():
    try:
        with open('personas.txt', 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        participantes = []
        for comentario in lineas:
            texto = comentario.strip()
            if len(texto) > 3:
                dni = texto[-3:]
                participantes.append((texto, dni))

        # Verificamos si hay suficientes participantes
        if len(participantes) < 3:
            messagebox.showerror("Error", "Se necesitan al menos 3 participantes.")
            return

        copia = participantes.copy()
        ganadores = random.sample(copia, 3)

        mensaje = ""
        for i, ganador in enumerate(ganadores):
            mensaje += f"Ganador {i + 1}: {ganador[0]}\n"

        messagebox.showinfo("GANADORES DEL SORTEO", mensaje)

    except FileNotFoundError:
        messagebox.showerror("Archivo no encontrado", "No se encontró el archivo personas.txt.")

# Crear ventana principal
root = tk.Tk()
root.title("Sorteo de Ganadores")

frame = tk.Frame(root, padx=50, pady=20)
frame.pack()

btn_sortear = tk.Button(frame, text="Realizar Sorteo", font=("Arial", 14), command=sortear_ganadores)
btn_sortear.pack()

root.mainloop()
