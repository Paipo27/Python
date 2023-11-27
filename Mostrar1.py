# import tkinter grafico
import tkinter as tk
#funcion para mostrar el primer elemento de la lista
def Mostrar():
    if data:
        label.config(text=data[0])
    else:
        label.config(text="Lista vacía")
# ventana principal
root = tk.Tk()
# titulo de la ventana
root.title("Mostrar Primer Elemento")
# lista de datos
data = ["perro", "gato", "conejo"]
button = tk.Button(root, text="Mostrar primer elemento", command=Mostrar)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()