"""nome = str(input('Qual seu nome? '))
print('Prazer em te conhecer, {:-<15} '.format(nome))
resposta Noah-----------
"""
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
soma = num1 + num2
subtracao = num1 - num2
multiplica = num1 * num2
divisao = num1 / num2
divisaointeira = num1 // num2
resto = num1 % num2
potencia = num1 ** num2
print('A soma entre {} e {} é {}. \nA subtração é {}.'.format(num1, num2, soma, subtracao))
print('A multiplicação entre {} e {} é {}. \nA divisão é {:.2f}. \nA divisão inteira é {}.'.format(num1, num2, multiplica, divisao, divisaointeira))
print('E o resto da divisão é {}.'.format(resto))
print('A potência é {}'.format(potencia))
