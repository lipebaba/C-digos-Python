salario=float(input('Digite seu salario:'))
prestação=float(input('Digite a prestação:'))

a=20*salario/100

if prestação > a:
    print('Emprestimo não pode ser consedido!')
else:
    print('Emprestimo pode ser concedio!')
    