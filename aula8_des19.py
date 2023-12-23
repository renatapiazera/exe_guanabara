import random

aluno1 = input('Aluno: ')
aluno2 = input('Aluno: ')
aluno3 = input('Aluno: ')
aluno4 = input('Aluno: ')
lista = [aluno4, aluno3, aluno2, aluno1]
escolha = random.choice(lista)
print('O sorteado foi {}'.format(escolha))
