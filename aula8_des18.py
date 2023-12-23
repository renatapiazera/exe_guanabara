import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno é {:.2f}'.format(cos))
print('A tangente é {:.2f}'.format(tan))
