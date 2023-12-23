dias = int(input('Quantos dias? '))
km = float(input('Quantos km ?'))
vdia = dias * 60
vkm = km * 0.15
print('O valor total é {:.2f}.'.format(vdia + vkm))