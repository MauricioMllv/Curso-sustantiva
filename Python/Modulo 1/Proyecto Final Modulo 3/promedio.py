import tkinter as tk
from tkinter import messagebox, simpledialog

class CalculadoraPromedioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Promedio")

        self.cantidad_notas_var = tk.IntVar()
        self.notas_var = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Calculadora de Promedio", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.root, text="Ingresar Cantidad de Notas", command=self.ingresar_cantidad).pack(pady=5)

        self.marco_notas = tk.Frame(self.root)
        self.marco_notas.pack(pady=10)

        tk.Button(self.root, text="Calcular Promedio", command=self.calcular_promedio).pack(pady=5)
        
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack(pady=10)
        
        tk.Button(self.root, text="Salir", command=self.salir_app).pack(pady=5)

    def ingresar_cantidad(self):
        cantidad_notas = simpledialog.askinteger("Ingresar Cantidad", "Ingrese la cantidad de notas:")
        if cantidad_notas is not None and cantidad_notas > 0:
            self.cantidad_notas_var.set(cantidad_notas)
            self.crear_campos_notas()

    def crear_campos_notas(self):
        for widget in self.marco_notas.winfo_children():
            widget.destroy()

        for i in range(self.cantidad_notas_var.get()):
            nota_var = tk.DoubleVar()
            self.notas_var.append(nota_var)
            tk.Label(self.marco_notas, text=f"Nota {i + 1}:").grid(row=i, column=0, padx=5, pady=5)
            entry_nota = tk.Entry(self.marco_notas, textvariable=nota_var)
            entry_nota.grid(row=i, column=1, padx=5, pady=5)

    def calcular_promedio(self):
        try:
            if self.cantidad_notas_var.get() > 0:
                notas = [nota_var.get() for nota_var in self.notas_var]
                promedio = sum(notas) / self.cantidad_notas_var.get()
                resultado = "Aprobado" if promedio >= 4.0 else "Reprobado"
                mensaje = f"El promedio del estudiante es: {promedio:.2f}\nResultado: {resultado}"
                self.resultado_label.config(text=mensaje)
            else:
                messagebox.showerror("Error", "Ingrese al menos una nota.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese notas válidas.")
    
    def salir_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    calculadora_gui = CalculadoraPromedioGUI(root)
    root.mainloop()
