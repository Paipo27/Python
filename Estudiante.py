import tkinter as tk
from tkinter import simpledialog

def add_student():
    name = simpledialog.askstring("Nombre", "Nombre del estudiante:")
    if name:
        grade = simpledialog.askfloat("Calificación", f"Calificación de {name}:")
        if grade is not None:
            students[name] = grade
            update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for name, grade in students.items():
        listbox.insert(tk.END, f"{name}: {grade}")

root = tk.Tk()
root.title("Tabla de Estudiantes")

students = {}

add_button = tk.Button(root, text="Añadir Estudiante", command=add_student)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()