# import para el tkinter grafico
import tkinter as tk
# import para los hilos
import threading
 # funcion para mostrar el primer elemento de la lista
def MostrarPrimerElemento():
    if data:
        label.config(text=data[0])
    else:
        label.config(text="Lista vacía")
# funcion para crear un hilo
def threadedPrimer():
    threading.Thread(target=MostrarPrimerElemento).start()
# ventana principal
root = tk.Tk()
root.title("Mostrar Primer Elemento")
data = ["perro", "gato", "conejo"]
button = tk.Button(root, text="Mostrar primer elemento", command=threadedPrimer)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()