def suma_numeros(values):
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total += v
    return total

def calcular_promedio(calificaciones):
    """Calcula el promedio de calificaciones validando que sean numeros"""
    try:
        total = suma_numeros(calificaciones)
        promedio = total / len(calificaciones)
        return promedio
    except TypeError as e:
        print(f'Error en las califficaciones: {e}')
        return None
    
# Ejemplos de uso
print("--- CALCULADORA DE PROMEDIOS ===")

# Caso exitoso
calificaciones_validas = [85, 90, 78, 92, 88]
promedio = calcular_promedio(calificaciones_validas)
if promedio:
    print(f"Promedio: {promedio:.2f}")

# Caso con error - contiene texto
calificaciones_invalidas = [85, 90, 'ausente', 92, 88]
promedio = calcular_promedio(calificaciones_invalidas)
if promedio:
    print("Promedio: {promedio:.2f}")
else:
    print("No se pudo calcular el promedio")

#Caso con error - contiene valor None
calificaciones_con_none = [85, 90, None, 92, 88]
promedio = calcular_promedio(calificaciones_con_none)



