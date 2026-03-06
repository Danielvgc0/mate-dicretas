import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        numero = int(entry_decimal.get())
        if numero < 0:
            messagebox.showerror("Error", "Por favor ingresa un número entero positivo.")
            return
        
        binario = bin(numero)[2:]
        label_resultado.config(text=f"Binario: {binario}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Convertidor Decimal a Binario")
ventana.geometry("350x200")
ventana.resizable(False, False)

# Título
label_titulo = tk.Label(ventana, text="Convertidor Decimal a Binario", font=("Arial", 14))
label_titulo.pack(pady=10)

# Entrada
label_decimal = tk.Label(ventana, text="Ingresa un número decimal:")
label_decimal.pack()

entry_decimal = tk.Entry(ventana)
entry_decimal.pack(pady=5)

# Botón
btn_convertir = tk.Button(ventana, text="Convertir", command=convertir)
btn_convertir.pack(pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="Binario: ", font=("Arial", 12))
label_resultado.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()
