def fibonacci(n):
    
    if n <= 0:
        return "Por favor, insira um número positivo."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequencia = [0, 1]
    for i in range(2, n):
        proximo_termo = sequencia[i - 1] + sequencia[i - 2]
        sequencia.append(proximo_termo)
    
    return sequencia

termos = int(input("Digite o número de termos para a sequência de Fibonacci: "))

resultado = fibonacci(termos)
print(f"A sequência de Fibonacci com {termos} termos é: {resultado}")
