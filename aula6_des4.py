n = input('Digite algo: ')
print('alfa numero?',n.isalnum())
print('alfabeto?', n.isalpha())
print('decimal?', n.isdecimal())
print(type(n))
print('Maiuscula?', n.isupper())
print('ascii', n.isascii())
print('digit', n.isdigit())
print('identifier', n.isidentifier())
print('CAPITALIZADA, a primeira maiuscula?', n.istitle())