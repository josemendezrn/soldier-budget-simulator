# Budget-Driven Unit Training Simulator

Este proyecto consiste en un script interactivo en Python diseñado para simular la **asignación dinámica de recursos (presupuesto)** y la generación estocástica de entidades de datos (unidades militares). El enfoque principal del desarrollo fue construir un sistema resiliente a fallos de usuario y estructurado de forma analítica.

---

## 🛠️ Características Técnicas y Enfoque Analítico

* **Generación Pseudoaleatoria de Atributos:** Uso de la librería `random` (`r.choice` y `r.randint`) para la simulación de variables cualitativas (roles de soldados) y cuantitativas discrecionales (costos de entrenamiento flotantes).
* **Validación de Entradas con Tolerancia a Fallos:** Implementación robusta de control de excepciones mediante bloques `try-except (ValueError)` montados sobre bucles interactivos. Esto asegura el *casting* correcto de tipos de datos (Strings a Integers) y mitiga colapsos del script ante errores del usuario final.
* **Estructura de Datos Indexada (JSON-like):** Los datos de cada entidad se capturan nativamente en diccionarios (`clave-valor`) enlazados a una clave primaria (`id`) secuencial autoincremental. Toda la muestra se almacena en una lista estructurada, óptima para futuras migraciones y análisis matriciales con Pandas.
* **Monitoreo de Presupuesto en Tiempo Real:** Algoritmo iterativo de decremento financiero (`monedas -= costo`) que evalúa la viabilidad presupuestaria en cada ciclo, aplicando un freno de mano lógico (`break`) al detectar fondos insuficientes.

---

## 📊 Arquitectura del Objeto Generado

Cada registro es procesado y empaquetado bajo la siguiente estructura de datos relacional:

```json
{
    "id": 1,
    "tipo": "Francotirador",
    "costo": 45
}

## 🚀 Cómo Ejecutar el Simulado
1. Clona este repositorio o descarga el código fuente.
2. Ejecuta el archivo desde tu terminal:
``` bash
    pytohn soldados.py
