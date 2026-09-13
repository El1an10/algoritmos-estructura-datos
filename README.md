# Algorithms & Data Structures

A collection of implementations built for the Algorithms and Data Structures course (Systems Engineering, UNAH). Includes advanced data structures written from scratch in Python, with no external libraries.

## Data structures

### `estructuras_de_datos/log_map/` — AVL tree (self-balancing ordered map)
A complete AVL tree implementation (`AVLTreeMap`) with single and double rotations, automatic rebalancing, and ordered-map operations (`find_le`, `find_lt`, `find_ge`, `find_gt`, `find_range`).

Built on top of it, `LogMap` is a specialized structure for indexing and querying log entries by date (`datetime`), with type validation on every operation.

**Complexity:** O(log n) guaranteed for insertion, search, and deletion, thanks to AVL balancing.

```python
from datetime import datetime
from estructuras_de_datos.log_map.log_map import LogMap

m = LogMap()
m[datetime(2026, 1, 5)] = "login failed"
m[datetime(2026, 1, 9)] = "disk warning"
m[datetime(2026, 1, 12)] = "server restart"

for k, v in m.find_range(datetime(2026, 1, 6), datetime(2026, 1, 13)):
    print(k.date(), "->", v)
```
```
2026-01-09 -> disk warning
2026-01-12 -> server restart
```

### `estructuras_de_datos/treque.py` — deque with middle insertion/deletion
A "treque" — a three-ended queue (front, back, and middle) — implemented with a doubly linked list.

- Operations at the ends (`insert_first`, `insert_last`, `delete_first`, `delete_last`): **O(1)**
- Operations in the middle (`insert_middle`, `delete_middle`): **O(n)**
- Custom exception handling (`Empty`) for operations on an empty structure.

```python
from estructuras_de_datos.treque import LinkedTreque

t = LinkedTreque()
t.insert_last(1)
t.insert_last(2)
t.insert_first(0)
t.insert_middle(99)

print(list(t.items()))
```
```
[0, 99, 1, 2]
```

## Algorithms

### `algoritmos/funciones.py`
- **`nro_de_salas`** — Determines the minimum number of rooms needed to schedule a set of meetings without overlap, using a sweep-line approach over start/end events.
- **`vuelto`** — Greedy currency-exchange algorithm, adapted to Honduran Lempira denominations.
- **`invierte_palabras`**, **`dibuja_rectangulo`** — String manipulation exercises.

```python
from algoritmos.funciones import vuelto, nro_de_salas

print(vuelto(87.50, 100))
print(nro_de_salas([(0, 30), (5, 10), (15, 20)]))
```
```
{10.0: 1, 2.0: 1, 0.5: 1}
2
```

## Exercises

Smaller exercises in control flow, exception handling, and functions (`ejercicios/`), used to practice input validation, error handling, and basic iterative structures.

## Running this

These are library modules (no `__main__` entry points), meant to be imported rather than run directly. Use them from a Python shell or script, as in the examples above — all standard Python (3.x), no external dependencies:

```bash
python -c "
from estructuras_de_datos.treque import LinkedTreque
t = LinkedTreque()
t.insert_last(1)
print(list(t.items()))
"
```

## Academic context

Developed as part of the Algorithms and Data Structures course, Systems Engineering program, Universidad Nacional Autónoma de Honduras (UNAH).
