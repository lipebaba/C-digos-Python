#Calculo do salário liquido de um professor

'''
Valor hora aula (Ensino Médio) = 30 reais
Aulas dadas = 100 por mês
Salário bruto = 3.000 reais
Desconto do INSS = 12%

'''

valor=float(input('Digite o valor da hora aula:'))
num=int(input('Digite o número de aulas dadas:'))
des=int(input('Digite o desconto do INSS:'))
a=valor*num
b=des*a/100
c=a-b
print('O seu salário liquido é: {}'.format(c))
