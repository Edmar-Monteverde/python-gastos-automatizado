import csv
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass(frozen=True)
class Gasto:  ## representa un gasto individual
    fecha: str
    categoria: str
    monto: float


class GestorGastos:
    def __init__(self, ruta_csv: str) -> None:
        self.ruta_csv = ruta_csv
        self.gastos: List[Gasto] = []

    def cargar(self) -> None:
        """Lee el CSV y carga los gastos en memoria (solo una vez por ejecución)."""
        self.gastos = []

        try:
            with open(self.ruta_csv, mode="r", encoding="utf-8") as file:
                lector = csv.DictReader(file)
                for fila in lector:
                    # Validación mínima
                    if (
                        "fecha" not in fila
                        or "categoria" not in fila
                        or "monto" not in fila
                    ):
                        continue

                    try:
                        monto = float(fila["monto"])
                    except ValueError:
                        continue  # salta filas con monto inválido
                        ## crear objeto Gasto y agregar a la lista
                    self.gastos.append(
                        Gasto(
                            fecha=fila["fecha"].strip(),
                            categoria=fila["categoria"].strip().lower(),
                            monto=monto,
                        )
                    )

        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"No se encontró el archivo: {self.ruta_csv}. Revisa la ruta."
            ) from e

    def imprimir(self) -> None:  ## imprime todos los gastos cargados
        for gasto in self.gastos:
            print(gasto)

    def total(self) -> float:
        return sum(
            g.monto for g in self.gastos
        )  ## calcula el total de todos los gastos

    def total_por_categoria(
        self,
    ) -> Dict[
        str, float
    ]:  ## calcula el total de gastos por categoría usando defaultdict
        acumulado: Dict[str, float] = defaultdict(float)
        for g in self.gastos:
            acumulado[g.categoria] += g.monto
        return dict(acumulado)

    def top_categorias(self, n: int = 3) -> List[Tuple[str, float]]:
        """Devuelve las N categorías con mayor gasto total."""
        resumen = self.total_por_categoria()  # dict[str, float]
        return sorted(resumen.items(), key=lambda item: item[1], reverse=True)[:n]

    def exportar_resumen(
        self, ruta_salida: str = "output/resumen.csv"
    ) -> None:  ## crear directorio si no existe y exportar resumen
        """Exporta un resumen por categoría a un CSV."""
        import os

        os.makedirs(
            os.path.dirname(ruta_salida), exist_ok=True
        )  ## Creamos la ruta de salida si no existe

        resumen = self.total_por_categoria()
        with open(
            ruta_salida, mode="w", encoding="utf-8", newline=""
        ) as file:  ## escribir encabezados y datos al archivo CSV
            writer = csv.writer(file)
            writer.writerow(["categoria", "total"])
            for categoria, total in sorted(resumen.items()):
                writer.writerow([categoria, f"{total:.2f}"])
