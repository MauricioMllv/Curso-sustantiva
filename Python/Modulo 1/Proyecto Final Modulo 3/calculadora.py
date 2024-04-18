import tkinter as tk
from tkinter import messagebox
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.entrada = tk.Entry(root, width=16, font=('Arial', 16))
        self.entrada.grid(row=0, column=0, columnspan=4)

        self.botones = [
            'C', '^', '√', 'Salir',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]

        self.row_val = 1
        self.col_val = 0

        for boton in self.botones:
            if boton == 'C':
                tk.Button(root, text=boton, width=4, height=2, command=self.borrar_todo).grid(row=self.row_val, column=self.col_val)
            elif boton == 'Salir':
                tk.Button(root, text=boton, width=4, height=2, command=self.salir_app).grid(row=self.row_val, column=self.col_val)
            
            elif boton == '<-':
                tk.Button(root, text=boton, width=4, height=2, command=self.borrar_ultimo).grid(row=self.row_val, column=self.col_val)
            elif boton == '^':
                tk.Button(root, text=boton, width=4, height=2, command=self.calcular_potencia).grid(row=self.row_val, column=self.col_val)
            elif boton == '√':
                tk.Button(root, text=boton, width=4, height=2, command=self.calcular_raiz_cuadrada).grid(row=self.row_val, column=self.col_val)
            else:
                tk.Button(root, text=boton, width=4, height=2, command=lambda btn=boton: self.agregar_numero(btn) if btn != '=' else self.calcular()).grid(row=self.row_val, column=self.col_val)
            
            self.col_val += 1
            if self.col_val > 3:
                self.col_val = 0
                self.row_val += 1

    def agregar_numero(self, numero):
        self.entrada.insert(tk.END, numero)

    def borrar_todo(self):
        self.entrada.delete(0, tk.END)

    def borrar_ultimo(self):
        self.entrada.delete(len(self.entrada.get()) - 1)

    def calcular(self):
        try:
            expresion = self.entrada.get()
            expresion = expresion.replace('^', '**')
            resultado = eval(expresion)
            self.borrar_todo()
            self.entrada.insert(tk.END, resultado)
        except Exception as e:
            self.borrar_todo()
            self.entrada.insert(tk.END, "Error")

    def calcular_potencia(self):
        try:
            numero = float(self.entrada.get())
            resultado = numero ** 2
            self.borrar_todo()
            self.entrada.insert(tk.END, resultado)
        except Exception as e:
            self.borrar_todo()
            self.entrada.insert(tk.END, "Error")

    def calcular_raiz_cuadrada(self):
        try:
            numero = float(self.entrada.get())
            resultado = math.sqrt(numero)
            self.borrar_todo()
            self.entrada.insert(tk.END, resultado)
        except Exception as e:
            self.borrar_todo()
            self.entrada.insert(tk.END, "Error")
            
    def salir_app(self):
        self.root.destroy()
