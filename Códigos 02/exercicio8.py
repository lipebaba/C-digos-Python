def eh_primo(n):
    if n <= 1:
        return False  
        return True 
    elif n % 2 == 0 or n % 3 == 0:
        return False 

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Digite um número para verificar se é primo: "))

if eh_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
