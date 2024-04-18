import tkinter as tk
from tkinter import messagebox

class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tareas = {}

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_nombre = tk.Label(self.frame, text="Nombre de tarea: ")
        self.label_nombre.grid(row=0, column=0, sticky='w')
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1)

        self.label_fecha = tk.Label(self.frame, text="Fecha de vencimiento: ")
        self.label_fecha.grid(row=1, column=0, sticky='w')
        self.entry_fecha = tk.Entry(self.frame)
        self.entry_fecha.grid(row=1, column=1)

        self.label_prioridad = tk.Label(self.frame, text="Prioridad, ingrese del 1 a 3\nSiendo 3 la más alta")
        self.label_prioridad.grid(row=2, column=0, sticky='w')
        self.entry_prioridad = tk.Entry(self.frame, validate="key", validatecommand=(self.root.register(self.validar_prioridad), '%P'))
        self.entry_prioridad.grid(row=2, column=1)

        self.button_agregar = tk.Button(self.frame, text="Agregar Tarea", command=self.agregar_tarea)
        self.button_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_mostrar = tk.Button(self.frame, text="Mostrar Tareas", command=self.mostrar_tareas)
        self.button_mostrar.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_limpiar = tk.Button(self.frame, text="Limpiar Campos", command=self.limpiar_campos)
        self.button_limpiar.grid(row=5, column=0, columnspan=2, pady=10)

        self.button_salir = tk.Button(self.frame, text="Salir", command=self.salir_app)
        self.button_salir.grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_tarea(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        prioridad = self.entry_prioridad.get()

        if nombre and fecha and prioridad:
            self.tareas[nombre] = {"Fecha de vencimiento": fecha, "Prioridad": prioridad}
            messagebox.showinfo("Tarea Agregada", f"Tarea '{nombre}' agregada con éxito.")
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")

    def mostrar_tareas(self):
        if self.tareas:
            tarea_texto = ""
            for nombre, detalles in self.tareas.items():
                tarea_texto += f"Nombre: {nombre} \nFecha de vencimiento: {detalles ['Fecha de vencimiento']} \nPrioridad: {detalles['Prioridad']}\n"
                messagebox.showinfo("Tareas", tarea_texto)
        else:
            messagebox.showinfo("Tarea", "No hay tareas registradas.")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_prioridad.delete(0, tk.END)
        self.entry_prioridad.tk.call(self.entry_prioridad._w, 'validate', 'set', '')
        self.entry_prioridad.tk.call(self.entry_prioridad._w, 'validate', 'key')

    def salir_app(self):
        self.root.destroy()

    def validar_prioridad(self, valor):
        try:
            prioridad = int(valor)
            if 1 <= prioridad <= 3:
                return True
            else:
                messagebox.showwarning("Error", "Ingrese número valido del 1 al 3")
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()
