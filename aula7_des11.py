alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
medida = alt * lar
tinta = medida / 2
print('A parede tem {:.2f}m².\nSerá necessário {:.2f}lt de tinta.'.format(medida, tinta))
