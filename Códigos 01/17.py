inf=int(input('Digite um número inferrior:'))
sup=int(input('Digite um número superior:'))

soma=0

for num in range(inf+1, sup):
    if num % 2 == 0:
        print(num)
        soma += num
        
print('Somatório dos números pares no intervalo:{}'.format(soma))
