import random

a1 = input('Aluno: ')
a2 = input('Aluno: ')
a3 = input('Aluno: ')
a4 = input('Aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem é: {}'.format(lista))
