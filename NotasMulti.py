#import tkinter grafica
import tkinter as tk
#simpledialog para crear cuadros de dialogo
from tkinter import simpledialog, messagebox
#import threading para crear hilos
import threading
#funcion para añadir notas
def add_note():
    title = simpledialog.askstring("Titulo", "¿Cuál es el título de la nota?")
    if title:
        content = simpledialog.askstring(f"Contenido - {title}", "Escribe el contenido de la nota:")
        if content:
            notes[title] = content
            Lista()
#funcion para ver notas
def Notas():
    threading.Thread(target=add_note).start()
#funcion para ver notas
def VerNota():
    title = listbox.get(listbox.curselection())
    if title in notes:
        messagebox.showinfo(title, notes[title])
#funcion de ver notas en hilo
def hilosNota():
    threading.Thread(target=VerNota).start()
#funcion para actualizar la lista
def Lista():
    listbox.delete(0, tk.END)
    for title in notes.keys():
        listbox.insert(tk.END, title)

root = tk.Tk()
root.title("Administrador de Notas Multihilado")

notes = {}

add_button = tk.Button(root, text="Añadir Nota", command=Notas)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

view_button = tk.Button(root, text="Ver Nota", command=hilosNota)
view_button.pack(pady=10)

root.mainloop()
