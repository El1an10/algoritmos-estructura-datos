def classification_n(numero):
    n_par = numero % 2 == 0
    n_multiplo_3 = numero % 3 == 0


    if n_par and n_multiplo_3:
        return "par y multiplo de 3"
    elif n_par: 
        return "solo par" 
    elif n_multiplo_3:
        return "solo multiplo de 3"
    else:
        return "Nada"
    
print("Escriba 'salir' para terminar el programa")

while True: 
    entrada = input("Ingrese un numero entero: ")
    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
    try: 
        numero = int(entrada)
        resultado = classification_n(numero)
        print(f"El numero {numero} es: {resultado}")
    except ValueError:
        print("Entrada invalida. Po favor ingrese un numero entrero o 'salir")
