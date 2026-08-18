def count(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

# Votos Recibidos
votos = ['Ana', 'Carlos', 'Ana', 'Maria', 'Carlos', 'Ana', 'Luis', 'Maria', 'Ana', 'Carlos']
candidatos = ['Ana', 'Carlos', 'Maria', 'Luis']

print("RESULTADOS DE LA VOTACION")
for candidato in candidatos:
    votos_obtenidos = count(votos, candidato)
    porcentaje = (votos_obtenidos / len(votos)) * 100
    print(f"{candidato}: {votos_obtenidos} votos ({porcentaje:.1f}%)")


calificaciones = [80, 90, 78, 85, 92, 78, 88, 85, 95, 78, 90, 85]

print("FRECUENCIA DE CADA CALIFICACION: ")
for nota in sorted(set(calificaciones)):
    frecuencia = count(calificaciones, nota)
    print(f"Nota {nota}: aparece {frecuencia} veces")


productos_vendidos = ['manzana', 'pan', 'leche', 'manzana', 'pan', 'manzana', 'huevos', 'leche', 'pan', 'manzana', 'leche', 'pan']
productos_inventario = ['manzana', 'pan', 'leche', 'huevos', 'queso']

print("VENTAS POR PRODUCTO:")
for producto in productos_inventario: 
    cantidad_vendida = count(productos_vendidos, producto)
    print(f"{producto.capitalize()}: {cantidad_vendida} unidades vendidas")