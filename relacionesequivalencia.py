import tkinter as tk
from tkinter import messagebox

def parse_set(text):
    return set(text.replace(" ", "").split(","))

def parse_relation(text):
    pares = text.replace(" ", "").split(";")
    relacion = set()
    for p in pares:
        a,b = p.split(",")
        relacion.add((a,b))
    return relacion

def es_reflexiva(A, R):
    for a in A:
        if (a,a) not in R:
            return False
    return True

def es_simetrica(R):
    for (a,b) in R:
        if (b,a) not in R:
            return False
    return True

def es_transitiva(R):
    for (a,b) in R:
        for (c,d) in R:
            if b == c and (a,d) not in R:
                return False
    return True

def verificar():
    try:
        A = parse_set(entry_conjunto.get())
        R = parse_relation(entry_relacion.get())

        reflexiva = es_reflexiva(A,R)
        simetrica = es_simetrica(R)
        transitiva = es_transitiva(R)

        resultado = f"""
Reflexiva: {reflexiva}
Simétrica: {simetrica}
Transitiva: {transitiva}
"""

        if reflexiva and simetrica and transitiva:
            resultado += "\nLa relación ES de equivalencia"
        else:
            resultado += "\nLa relación NO es de equivalencia"

        label_resultado.config(text=resultado)

    except:
        messagebox.showerror("Error", "Formato incorrecto")

ventana = tk.Tk()
ventana.title("Relación de Equivalencia")
ventana.geometry("420x320")
ventana.config(bg="#2C3E50")   # color de fondo de la ventana

titulo = tk.Label(
    ventana,
    text="Verificador de Relaciones",
    bg="#2C3E50",
    fg="white",
    font=("Arial",16,"bold")
)
titulo.pack(pady=10)

tk.Label(
    ventana,
    text="Conjunto A (ej: a,b,c)",
    bg="#2C3E50",
    fg="white"
).pack()

entry_conjunto = tk.Entry(
    ventana,
    width=40,
    bg="#ECF0F1"
)
entry_conjunto.pack(pady=5)

tk.Label(
    ventana,
    text="Relación R (ej: a,a;a,b;b,a)",
    bg="#2C3E50",
    fg="white"
).pack()

entry_relacion = tk.Entry(
    ventana,
    width=40,
    bg="#ECF0F1"
)
entry_relacion.pack(pady=5)

boton = tk.Button(
    ventana,
    text="Verificar relación",
    bg="#3498DB",
    fg="white",
    font=("Arial",10,"bold"),
    activebackground="#2980B9",
    command=verificar
)
boton.pack(pady=15)

label_resultado = tk.Label(
    ventana,
    text="",
    bg="#2C3E50",
    fg="#F1C40F",
    justify="left",
    font=("Arial",10)
)
label_resultado.pack()

ventana.mainloop()