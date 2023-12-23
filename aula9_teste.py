nome = input('Nome completo: ')

print('Nome: {}'.format('-'.join(nome)))
print('Nome maiúsculo: {}.'.format(nome.upper()))
print('Nome minúsculo: {}.'.format(nome.lower()))
print('Nova função, somente a primeira maiúscula: {}'.format(nome.capitalize()))
print('Agora somente a primeira maiúscula de cada palavra: {}'.format(nome.title()))
print('Remove espaços inúteis antes e depois da frase: {}'.format(nome.strip()))
print('Remove espaços do final da frase: {}'.format(nome.rstrip()))
print('Remove espaços do início da frase: {}'.format(nome.lstrip()))
print('Total de {} letras no nome e no sobrenome.'.format(len(nome)))

print(nome[3]) #mostra a string 3
print(nome[:3]) #mostra a string do zero ate uma antes da 3
print(nome[4:]) #mostra as strings do 4 até o final
print(nome[3:6]) #mostra da string 3 até uma antes da sexta
print(nome[3:7:2]) #mostra da string 3 até uma antes da 7, de 2 em 2
print(nome.count('a')) #conta quantos a minúsculo tem
print(nome.upper().count('A'))
print(len(nome.strip()))
print(len(nome))
print(nome.replace('Renata', 'Noah'))
nome = nome.replace('Renata','Noah')
print(nome)
print(nome.split())