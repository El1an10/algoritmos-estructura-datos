def invertir_palabras(palabra):
    pila = []
    for c in palabra:
        pila.append (c)
    muestra = ''

    while pila:
        muestra += pila.pop()
    return muestra

print(invertir_palabras("ejemplo"))
    
    
        


