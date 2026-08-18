# Algoritmos y Estructuras de Datos

Colección de implementaciones desarrolladas en el curso de Algoritmos y Estructura de Datos (Ingeniería en Sistemas Computacionales, UNAH). Incluye estructuras de datos avanzadas construidas desde cero en Python, sin librerías externas.

## Estructuras de datos

### `estructuras_de_datos/log_map/` — Árbol AVL (mapa ordenado autobalanceado)
Implementación completa de un árbol AVL (`AVLTreeMap`) con rotaciones simples y dobles, rebalanceo automático, y operaciones de mapa ordenado (`find_le`, `find_lt`, `find_ge`, `find_gt`, `find_range`).

Sobre esa base se construyó `LogMap`: una estructura especializada para indexar y consultar entradas de log por fecha (`datetime`), con validación de tipos en cada operación.

**Complejidad:** O(log n) garantizado en inserción, búsqueda y eliminación, gracias al balanceo AVL.

### `estructuras_de_datos/treque.py` — Deque con inserción/eliminación al medio
Estructura de datos tipo "treque": una cola de tres extremos (inicio, final y medio), implementada con lista doblemente enlazada.

- Operaciones en los extremos (`insert_first`, `insert_last`, `delete_first`, `delete_last`): **O(1)**
- Operaciones al medio (`insert_middle`, `delete_middle`): **O(n)**
- Manejo de excepciones propio (`Empty`) para operaciones sobre estructura vacía.

## Algoritmos

### `algoritmos/funciones.py`
- **`nro_de_salas`** — Determina el número mínimo de salas necesarias para agendar un conjunto de reuniones sin solapamiento, usando un enfoque de línea de barrido (*sweep line*) sobre eventos de inicio/fin.
- **`vuelto`** — Algoritmo greedy de cambio de moneda, adaptado a denominaciones de Lempiras hondureñas.
- **`invierte_palabras`**, **`dibuja_rectangulo`** — Ejercicios de manipulación de cadenas.

## Ejercicios

Ejercicios menores de control de flujo, manejo de excepciones y funciones (`ejercicios/`), usados para practicar validación de entradas, manejo de errores y estructuras iterativas básicas.

## Cómo ejecutar

Todos los scripts son Python estándar (3.x), sin dependencias externas:

```bash
python estructuras_de_datos/treque.py
python estructuras_de_datos/log_map/log_map.py
python algoritmos/funciones.py
```

## Contexto académico

Desarrollado como parte del curso de Algoritmos y Estructura de Datos de la carrera de Ingeniería en Sistemas Computacionales, Universidad Nacional Autónoma de Honduras (UNAH).
