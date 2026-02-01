# 📊 Python – Gestor de Gastos Automatizado

Herramienta en Python para **procesar archivos CSV de gastos**, calcular totales,
agrupar por categoría, mostrar rankings y **exportar resúmenes automáticamente**.
El proyecto está diseñado como una **utilidad reutilizable por línea de comandos**.

---

## 🚀 Funcionalidades

- 📥 Carga gastos desde un archivo CSV
- 📊 Calcula el total de gastos
- 🗂️ Agrupa gastos por categoría
- 🏆 Muestra el Top N de categorías con mayor gasto
- 📄 Exporta un resumen a CSV
- ⚙️ Configuración por línea de comandos (`argparse`)
- 🧱 Código estructurado con POO (Programación Orientada a Objetos)
- ✅ Validación fuerte del archivo CSV (columnas requeridas, formato de fecha, montos inválidos)


## 📁 Estructura del proyecto

python-gastos-automatizado/
│
├── data/
│ └── gastos.csv
│
├── src/
│ ├── gestor_gastos.py
│ └── main.py
│
├── output/
│ └── resumen.csv # (no versionado)
│
├── .gitignore
└── README.md


---

## 📝 Formato del CSV de entrada

El archivo CSV debe contener las siguientes columnas:

```csv
fecha,categoria,monto
2026-01-01,comida,12.50
2026-01-01,transporte,3.20
```


fecha: string (YYYY-MM-DD)

categoria: string

monto: número decimal

⚠️ El programa valida que el archivo CSV contenga las columnas requeridas
y que los datos tengan el formato correcto.  
Las filas inválidas son omitidas y se informa al usuario.


---
### ▶️ Uso

```bash
Desde la raíz del proyecto, ejecuta:

 ▶️Usar valores por defecto: 

📌 python src/main.py


▶️Especificar archivo de entrada y salida: 

📌python src/main.py --input data/gastos.csv --output output/resumen.csv


▶️Mostrar solo el Top 2 de categorías y no imprimir todos los gastos 

📌 python src/main.py --top 2 --no-print
```
## ⚙️ Argumentos disponibles

| Argumento    | Descripción                          |
| ------------ | ------------------------------------ |
| `--input`    | Ruta del CSV de entrada              |
| `--output`   | Ruta del CSV de salida               |
| `--top`      | Cantidad de categorías a mostrar     |
| `--no-print` | No imprime todos los gastos cargados |




## 🧠 Tecnologías usadas

- Python 3
- Programación Orientada a Objetos (POO)
- csv
- argparse
- dataclasses
- defaultdict
- Git & GitHub




## 🎯 Objetivo del proyecto

Este proyecto fue desarrollado con fines de **aprendizaje y portafolio**, con el objetivo de:

- Practicar automatización y procesamiento de datos en Python
- Aplicar Programación Orientada a Objetos en un caso real
- Crear una herramienta reutilizable mediante línea de comandos
- Adquirir buenas prácticas de desarrollo y control de versiones con Git



## 📌 Posibles mejoras futuras

- Filtros por fecha (--desde, --hasta)

- Tests automatizados

Soporte para otros formatos (Excel)
## 🧠 Aprendizajes clave

Durante el desarrollo de este proyecto se reforzaron y aplicaron los siguientes conceptos:

- 📌 Lectura y procesamiento de archivos CSV en Python
- 📌 Modelado de datos usando Programación Orientada a Objetos (`dataclass`)
- 📌 Separación de responsabilidades (carga, procesamiento y salida de datos)
- 📌 Uso de `defaultdict` para agrupaciones y acumulaciones eficientes
- 📌 Ordenamiento de datos usando funciones `lambda`
- 📌 Creación de herramientas configurables por línea de comandos con `argparse`
- 📌 Manejo de errores y validaciones básicas de datos
- 📌 Uso de Git con commits incrementales durante el desarrollo
- 📌 Escritura de documentación clara orientada a usuarios y reclutadores
- 📌 Implementación de validaciones fuertes y manejo de excepciones personalizadas


Este proyecto ayudó a entender cómo transformar un script simple en una **herramienta reutilizable y mantenible**, similar a las utilizadas en entornos reales de trabajo.



👤 Autor

Edmar Monteverde