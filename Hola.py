print("mi primer programa en python")
print(4+5)
import tkinter as tk
from tkinter import messagebox


class BinarioDecimalApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Convertidor Binario a Decimal")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self._crear_widgets()

    def _crear_widgets(self) -> None:
        # Título
        titulo = tk.Label(
            self.root,
            text="Convertidor Binario → Decimal",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=15)

        # Entrada
        self.entrada_binario = tk.Entry(
            self.root,
            font=("Arial", 12),
            justify="center"
        )
        self.entrada_binario.pack(pady=10)

        # Botón
        boton_convertir = tk.Button(
            self.root,
            text="Convertir",
            font=("Arial", 11),
            command=self.convertir
        )
        boton_convertir.pack(pady=10)

        # Resultado
        self.label_resultado = tk.Label(
            self.root,
            text="Resultado: ",
            font=("Arial", 12)
        )
        self.label_resultado.pack(pady=10)

    def validar_binario(self, binario: str) -> bool:
        return all(bit in "01" for bit in binario)

    def convertir(self) -> None:
        binario = self.entrada_binario.get().strip()

        if not binario:
            messagebox.showwarning("Advertencia", "Ingresa un número binario.")
            return

        if not self.validar_binario(binario):
            messagebox.showerror("Error", "Solo se permiten 0 y 1.")
            return

        decimal = int(binario, 2)
        self.label_resultado.config(text=f"Resultado: {decimal}")


def main():
    root = tk.Tk()
    app = BinarioDecimalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
