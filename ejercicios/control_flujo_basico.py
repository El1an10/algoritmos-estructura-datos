suma = 0
print("Ingrese numeros positivos. Escriba 0 para terminar.")
print("Los numeros negativos seran ignorados.")
print("El programa se detendra si la suma supera 100.")

while True:
    numero = int(input("Ingrese un numero: "))

    #Si es 0 termina el ciclo
    if numero == 0:
        print("Se ingreso 0. Terminando...")
        break

    #Si es un numero negativo, lo ignora con continue
    if numero < 0:
        print(f"Numero {numero} ignorado (es negativo)")
        continue

    #Si es positivo, lo suma
    suma += numero
    print(f"Suma actual: {suma}")
    

    # Si la suma supera 100, rompe el ciclo
    if suma > 100:
        print("La suma supero 100! Rompiendo el ciclo...")
        break

print(f"suma final: {suma}")