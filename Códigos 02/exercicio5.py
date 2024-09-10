quant_posi = 0

while True:
    num=float(input('Digite um número(ou um negativo para sair):'))
    if num < 0:
        quant_posi += 1
        print('Quantiade de números positivos digitados = {}'.format(quant_posi))

