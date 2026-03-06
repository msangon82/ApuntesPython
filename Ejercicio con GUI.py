import random
import tkinter as tk
from tkinter import messagebox


class Concurso:
    puertas = [1, 2, 3]

    def __init__(self, iteraciones: int):
        self.iteraciones = iteraciones
        self.gana_mantener = 0
        self.gana_cambiar = 0
        self.jugadas_mantener = 0
        self.jugadas_cambiar = 0

    def simular_una_ronda(self) -> None:
        premio = random.choice(self.puertas)
        eleccion_jugador = random.choice(self.puertas)

        # El presentador abre una puerta vacia que no eligio el jugador.
        opciones_presentador = [
            puerta
            for puerta in self.puertas
            if puerta != eleccion_jugador and puerta != premio
        ]
        puerta_abierta = random.choice(opciones_presentador)

        cambia = random.choice([True, False])

        if cambia:
            self.jugadas_cambiar += 1
            nueva_eleccion = next(
                puerta
                for puerta in self.puertas
                if puerta != eleccion_jugador and puerta != puerta_abierta
            )
            if nueva_eleccion == premio:
                self.gana_cambiar += 1
        else:
            self.jugadas_mantener += 1
            if eleccion_jugador == premio:
                self.gana_mantener += 1

    def ejecutar(self) -> None:
        for _ in range(self.iteraciones):
            self.simular_una_ronda()

    def informe(self):
        pct_mantener = (
            (self.gana_mantener / self.jugadas_mantener) * 100
            if self.jugadas_mantener > 0
            else 0.0
        )
        pct_cambiar = (
            (self.gana_cambiar / self.jugadas_cambiar) * 100
            if self.jugadas_cambiar > 0
            else 0.0
        )
        return pct_mantener, pct_cambiar


class AppMontyHall:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simulador Monty Hall")
        self.root.geometry("420x260")
        self.root.resizable(False, False)

        marco = tk.Frame(root, padx=16, pady=16)
        marco.pack(fill="both", expand=True)

        titulo = tk.Label(
            marco,
            text="Concurso Monty Hall",
            font=("Segoe UI", 16, "bold"),
        )
        titulo.pack(pady=(0, 12))

        fila = tk.Frame(marco)
        fila.pack(pady=6)

        tk.Label(fila, text="Numero de iteraciones:", font=("Segoe UI", 11)).pack(
            side="left", padx=(0, 8)
        )

        self.entrada_iteraciones = tk.Entry(fila, width=14, font=("Segoe UI", 11))
        self.entrada_iteraciones.pack(side="left")
        self.entrada_iteraciones.insert(0, "10000")

        boton = tk.Button(
            marco,
            text="Simular",
            font=("Segoe UI", 11, "bold"),
            command=self.ejecutar_simulacion,
        )
        boton.pack(pady=12)

        self.resultado_mantener = tk.Label(
            marco,
            text="Ganando al mantener: -",
            font=("Segoe UI", 11),
            anchor="w",
            justify="left",
        )
        self.resultado_mantener.pack(fill="x", pady=4)

        self.resultado_cambiar = tk.Label(
            marco,
            text="Ganando al cambiar: -",
            font=("Segoe UI", 11),
            anchor="w",
            justify="left",
        )
        self.resultado_cambiar.pack(fill="x", pady=4)

    def ejecutar_simulacion(self) -> None:
        valor = self.entrada_iteraciones.get().strip()

        if not valor.isdigit() or int(valor) <= 0:
            messagebox.showerror("Error", "Ingresa un numero entero positivo.")
            return

        iteraciones = int(valor)
        concurso = Concurso(iteraciones)
        concurso.ejecutar()

        pct_mantener, pct_cambiar = concurso.informe()

        self.resultado_mantener.config(
            text=(
                f"Ganando al mantener: {pct_mantener:.2f}% "
                f"({concurso.gana_mantener}/{concurso.jugadas_mantener})"
            )
        )
        self.resultado_cambiar.config(
            text=(
                f"Ganando al cambiar: {pct_cambiar:.2f}% "
                f"({concurso.gana_cambiar}/{concurso.jugadas_cambiar})"
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = AppMontyHall(root)
    root.mainloop()
