import tkinter as tk

# funciones logicas
def AND(a,b):
    return int(a and b)

def OR(a,b):
    return int(a or b)

def NOT(a):
    return int(not a)

# funcion para mostrar la tabla AND
def mostrar_and():
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, "Tabla de verdad AND\n")
    resultado.insert(tk.END, "A B | A AND B\n")
    
    for A in [0,1]:
        for B in [0,1]:
            linea = f"{A} {B} | {AND(A,B)}\n"
            resultado.insert(tk.END, linea)

# ventana principal
ventana = tk.Tk()
ventana.title("Compuertas Logicas")
ventana.geometry("300x250")

# boton
boton_and = tk.Button(ventana, text="Mostrar tabla AND", command=mostrar_and)
boton_and.pack(pady=10)

# area de texto para mostrar resultados
resultado = tk.Text(ventana, height=10, width=25)
resultado.pack()

# ejecutar ventana
ventana.mainloop()