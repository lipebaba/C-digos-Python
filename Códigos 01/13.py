import math

num=float(input('Digite um número:'))

if num >= 0:
    a=math.sqrt(num)
    print('A raiz quadrada é = {}'.format(a))
else:
    b=num**2
    print('O quadrado é = {}'.format(b))
