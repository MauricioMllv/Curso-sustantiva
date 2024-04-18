import tkinter as tk
from tkinter import messagebox, simpledialog

class AgendaContactosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos")

        self.agenda = AgendaContactos()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Agenda de Contactos", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.root, text="Agregar Contacto", command=self.agregar_contacto).pack(pady=5)
        tk.Button(self.root, text="Ver Contactos", command=self.ver_contactos).pack(pady=5)
        tk.Button(self.root, text="Buscar Contacto", command=self.buscar_contacto).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.destroy).pack(pady=5)

    def agregar_contacto(self):
        nombre = simpledialog.askstring("Agregar Contacto", "Ingrese el nombre del contacto:")
        if nombre:
            telefono = simpledialog.askstring("Agregar Contacto", "Ingrese el número de teléfono:")
            if telefono:
                self.agenda.agregar_contacto(nombre, telefono)
                messagebox.showinfo("Éxito", f"Contacto {nombre} agregado correctamente.")
            else:
                messagebox.showwarning("Error", "Debe ingresar un número de teléfono.")
        else:
            messagebox.showwarning("Error", "Debe ingresar un nombre.")

    def ver_contactos(self):
        contactos = self.agenda.ver_contactos()
        if not contactos:
            messagebox.showinfo("Agenda de Contactos", "La agenda está vacía.")
        else:
            messagebox.showinfo("Agenda de Contactos", f"Lista de contactos:\n{contactos}")

    def buscar_contacto(self):
        nombre = simpledialog.askstring("Buscar Contacto", "Ingrese el nombre del contacto a buscar:")
        if nombre:
            contacto = self.agenda.buscar_contacto(nombre)
            if contacto:
                messagebox.showinfo("Contacto Encontrado", f"Nombre: {nombre}, Teléfono: {contacto}")
            else:
                messagebox.showinfo("Contacto no encontrado", f"El contacto {nombre} no se encuentra en la agenda.")

class AgendaContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def ver_contactos(self):
        if not self.contactos:
            return None
        else:
            contactos_str = "\n".join([f"{nombre}: {telefono}" for nombre, telefono in self.contactos.items()])
            return contactos_str

    def buscar_contacto(self, nombre):
        return self.contactos.get(nombre, None)

if __name__ == "__main__":
    root = tk.Tk()
    agenda_gui = AgendaContactosGUI(root)
    root.mainloop()
