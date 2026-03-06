import tkinter as tk
from tkinter import ttk, messagebox


def bin_to_dec(value):
    return str(int(value, 2))


def dec_to_bin(value):
    return bin(int(value))[2:]


def hex_to_oct(value):
    return oct(int(value, 16))[2:]


def oct_to_hex(value):
    return hex(int(value, 8))[2:].upper()


def convert():
    value = entry.get().strip()
    conversion = combo.get()

    try:
        if conversion == "Binario a Decimal":
            result = bin_to_dec(value)
        elif conversion == "Decimal a Binario":
            result = dec_to_bin(value)
        elif conversion == "Hexadecimal a Octal":
            result = hex_to_oct(value)
        elif conversion == "Octal a Hexadecimal":
            result = oct_to_hex(value)
        else:
            result = "Error"

        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Entrada inválida")


root = tk.Tk()
root.title("Conversor")
root.geometry("400x250")

combo = ttk.Combobox(
    root,
    values=[
        "Binario a Decimal",
        "Decimal a Binario",
        "Hexadecimal a Octal",
        "Octal a Hexadecimal"
    ],
    state="readonly"
)
combo.pack(pady=10)
combo.current(0)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Convertir", command=convert).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()


