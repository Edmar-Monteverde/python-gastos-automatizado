import argparse
from gestor_gastos import GestorGastos, CSVInvalidoError


def leer_argumentos() -> argparse.Namespace:
    ## Crear el parser de argumentos que sirve para ejecutar el programa desde línea de comandos y no depender de una ruta fija
    parse = argparse.ArgumentParser(
        description="Gestor de gastos desde un archivo CSV."
    )

    parse.add_argument(
        "--input",
        default="data/gastos.csv",
        help="Ruta al archivo CSV de entrada( default: data/gastos.csv).",
    )

    parse.add_argument(
        "--output",
        default="output/resumen.csv",
        help="Ruta al archivo CSV de salida (default: output/resumen.csv).",
    )

    parse.add_argument(
        "--top",
        type=int,
        default=3,
        help="Número de categorías principales a mostrar (default: 3).",
    )

    parse.add_argument(
        "--no-print", action="store_true", help="No imprimir los gastos cargados."
    )
    return parse.parse_args()


def main() -> None:

    args = leer_argumentos()  ## leer argumentos desde línea de comandos

    gestor = GestorGastos(args.input)
    try:
        gestor.cargar()
    except CSVInvalidoError as e:
        print(f"❌ Error en el archivo CSV: {e}")
        return  # Salir si no se encuentra el archivo

    if not args.no_print:
        print("\n--- GASTOS CARGADOS ---")
        gestor.imprimir()

    print("\n--- TOTAL ---")
    print(f"Total de gastos: {gestor.total():.2f}")

    print("\n--- TOTAL POR CATEGORÍA ---")

    por_cat = gestor.total_por_categoria()
    for cat, total in sorted(por_cat.items()):
        print(f"{cat}: {total:.2f}")

    print(f"\n--- TOP {args.top} CATEGORÍAS ---")
    top_cats = gestor.top_categorias(args.top)
    for cat, total in top_cats:
        print(f"{cat}: {total:.2f}")

    gestor.exportar_resumen(args.output)
    print(f"\n✅ Resumen exportado a: {args.output}")


if __name__ == "__main__":
    main()
