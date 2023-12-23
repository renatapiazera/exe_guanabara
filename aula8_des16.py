import math

num = float(input('Digite um número real: '))
#print('O número digitado é {}'.format(math.floor(num))) #arredondar para menos
print('O número digitado foi {}, e o inteiro dele é {}'.format(num, (math.trunc(num))))
#math.trunc arredonda o número real