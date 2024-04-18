import tkinter as tk

def agregar_numero(numero):
    entrada.insert(tk.END, numero)

def borrar_todo():
    entrada.delete(0, tk.END)

def borrar_ultimo():
    entrada.delete(len(entrada.get()) - 1)

def calcular():
    try:
        resultado = eval(entrada.get())
        borrar_todo()
        entrada.insert(tk.END, resultado)
    except Exception as e:
        borrar_todo()
        entrada.insert(tk.END, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, width=16, font=('Arial', 16))
entrada.grid(row=0, column=0, columnspan=4)

botones = [
    'C', '', '', '',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for boton in botones:
    if boton == 'C':
        tk.Button(ventana, text=boton, width=4, height=2, command=borrar_todo).grid(row=row_val, column=col_val)
    elif boton == '<-':
        tk.Button(ventana, text=boton, width=4, height=2, command=borrar_ultimo).grid(row=row_val, column=col_val)
    else:
        tk.Button(ventana, text=boton, width=4, height=2, command=lambda btn=boton: agregar_numero(btn) if btn != '=' else calcular()).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ventana.mainloop()
