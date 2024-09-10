def exibir_tabuada(n):
    print(f"Tabuada de {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

numero = int(input("Digite um número para ver a tabuada: "))

exibir_tabuada(numero)
