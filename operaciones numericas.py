import tkinter
from tkinter import messagebox

def calcular():
    sistema = sistema_var.get()
    num1 = entrada1.get()
    num2 = entrada2.get()
    operacion = operacion_var.get()

    if sistema == "Binario":
        base = 2
    elif sistema == "Octal":
        base = 8
    else:
        base = 16

    try:
        n1 = int(num1, base)
        n2 = int(num2, base)

        if operacion == "+":
            resultado = n1 + n2
        elif operacion == "-":
            resultado = n1 - n2
        elif operacion == "*":
            resultado = n1 * n2
        elif operacion == "/":
            if n2 == 0:
                messagebox.showerror("Error", "No dividir entre cero")
                return
            resultado = n1 // n2

        if base == 2:
            salida = bin(resultado)[2:]
        elif base == 8:
            salida = oct(resultado)[2:]
        else:
            salida = hex(resultado)[2:].upper()

        resultado_label.config(text=salida)

    except:
        messagebox.showerror("Error", "Dato inválido")


# Ventana
ventana = tkinter.Tk()
ventana.title("Calculadora de Bases")
ventana.geometry("350x300")
ventana.configure(bg="lightblue")


# Sistema numérico
tkinter.Label(ventana, text="Sistema").pack()
sistema_var = tkinter.StringVar()
sistema_var.set("Binario")

tkinter.OptionMenu(ventana, sistema_var, "Binario", "Octal", "Hexadecimal").pack()

# Número 1
tkinter.Label(ventana, text="Primer número").pack()
entrada1 = tkinter.Entry(ventana)
entrada1.pack()

# Operación
tkinter.Label(ventana, text="Operación").pack()
operacion_var = tkinter.StringVar()
operacion_var.set("+")
tkinter.OptionMenu(ventana, operacion_var, "+", "-", "*", "/").pack()

# Número 2
tkinter.Label(ventana, text="Segundo número").pack()
entrada2 = tkinter.Entry(ventana)
entrada2.pack()

# Botón
tkinter.Button(
    ventana,
    text="Calcular",
    command=calcular,
    bg="blue",       # color del botón
    fg="white"       # color del texto
).pack(pady=10)


# Resultado
tkinter.Label(ventana, text="Resultado").pack()
resultado_label = tkinter.Label(ventana, text="", fg="blue")
resultado_label.pack()

ventana.mainloop()


