import tkinter as tk
from tkinter import messagebox
from calculadora import Calculadora
from gestor_avanzado import GestorTareasApp
from contactos import AgendaContactosGUI
from promedio import CalculadoraPromedioGUI

class Programa:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Programa")

        self.contactos = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Gestión de Tareas \n ", font=("Helvetica", 16)).pack(padx=50)

        tk.Button(self.root, text="Gestor de Tareas", command=self.gestion_tareas).pack(padx=5, pady=10)
        tk.Button(self.root, text="Calculadora Avanzada", command=self.abrir_calculadora).pack(padx=5, pady=10)
        tk.Button(self.root, text="Registrar Contacto", command=self.registrar_contacto).pack(padx=5, pady=10)
        tk.Button(self.root, text="Calcular Notas", command=self.calcular_notas).pack(padx=5, pady=10)
        tk.Button(self.root, text="Salir", command=self.salir_app).pack(padx=5, pady=10)

    def gestion_tareas(self):
        gestion_window = tk.Toplevel(self.root)
        gestor_avanzado = GestorTareasApp(gestion_window)

    def abrir_calculadora(self):
        calculadora_window = tk.Toplevel(self.root)
        calculadora = Calculadora(calculadora_window)

    def registrar_contacto(self):
        contactos_window = tk.Toplevel(self.root)
        contactos = AgendaContactosGUI(contactos_window)

    def calcular_notas(self):
        calcular_window = tk.Toplevel(self.root)
        promedio = CalculadoraPromedioGUI(calcular_window)

    def salir_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    programa = Programa(root)
    root.mainloop()

