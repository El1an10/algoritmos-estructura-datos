def invierte_palabras(entrada):
    """Escriba el código de la función invierte palabras, que recibe una cadena de
    palabras separadas por espacios y retorna otra cadena con las mismas palabras
    pero cada una con el orden de los caracteres que la forman invertidas.
    
    Ejemplo:
    invierte_palabras("buenas noches mucho gusto") -> "saneub sehcon ohcum otsug"
    """
    palabras = entrada.split()
    resultado = ""
    
    for i in range(len(palabras)):
        palabra_invertida = palabras[i][::-1]
        if i > 0:
            resultado += " "
        resultado += palabra_invertida
    
    return resultado


def dibuja_rectangulo(alto, ancho):
    """Esta función dibuja utilizando asteriscos, el rectángulo con las medidas que
    se le indica en los parámetros y retorna (no imprime) un string conteniendo
    tres tipos de caracteres: asterisco, espacio en blanco y salto de línea.
    
    Ejemplo:
    dibuja_rectangulo(3, 5) ->
    *****
    *   *
    *****
    """
    rectangulo = ""
    
    for fila in range(alto):
        if fila == 0 or fila == alto - 1:
            # Primera y última fila
            for col in range(ancho):
                rectangulo += "*"
            rectangulo += "\n"
        else:
            # Filas del medio
            rectangulo += "*"
            for col in range(ancho - 2):
                rectangulo += " "
            rectangulo += "*"
            rectangulo += "\n"
    
    return rectangulo


def nro_de_salas(reuniones):
    """Esta función retorna el número mínimo de salas que se necesitan para
    que se puedan realizar todas las reuniones que se reciben. Las reuniones
    se representan como una lista de tuplas, donde cada tupla contiene
    la hora de inicio y fin de la reunión como números enteros."""
    
    if len(reuniones) == 0:
        return 0
    
    eventos = []
    for reunion in reuniones:
        inicio = reunion[0]
        fin = reunion[1]
        eventos.append((inicio, 'i'))
        eventos.append((fin, 'f'))
    
    eventos.sort()
    
    salas_actuales = 0
    maximo_salas = 0
    
    for evento in eventos:
        hora = evento[0]
        tipo = evento[1]
        
        if tipo == 'i':
            salas_actuales = salas_actuales + 1
            if salas_actuales > maximo_salas:
                maximo_salas = salas_actuales
        else:
            salas_actuales = salas_actuales - 1
    
    return maximo_salas


def vuelto(cantidad_pagar, cantidad_entregada):
    """Retorna un diccionario con la cantidad de billetes y monedas que deben ser entregas como
    vuelto a un cliente."""
    
    # Calcular cuanto vuelto hay que dar
    diferencia = cantidad_entregada - cantidad_pagar
    
    # Convertir a centavos para evitar problemas con decimales
    vuelto_centavos = round(diferencia * 100)
    
    if vuelto_centavos <= 0:
        return {}
    
    # Denominaciones en centavos (de mayor a menor)
    denoms_centavos = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 25, 10, 5, 2, 1]
    denoms_lempiras = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.25, 0.10, 0.05, 0.02, 0.01]
    
    vuelto_dict = {}
    
    for i in range(len(denoms_centavos)):
        denominacion_centavos = denoms_centavos[i]
        denominacion_lempiras = denoms_lempiras[i]
        
        # Cuantas de esta denominación caben
        cantidad = vuelto_centavos // denominacion_centavos
        
        if cantidad > 0:
            vuelto_dict[denominacion_lempiras] = cantidad
            # Actualizar el vuelto restante
            vuelto_centavos = vuelto_centavos % denominacion_centavos
    
    return vuelto_dict
