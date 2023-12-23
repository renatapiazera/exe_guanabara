valor = float(input('Qual o valor? '))
desconto = valor - (valor * (5/100))
print('O valor com o desconto ficará R${:.2f}.'.format(desconto))
