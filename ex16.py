# faça um programa que leia a largura e altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input('informe a largura da parede em metros: '))
a = float(input('informe a altura da parede em metros: '))
# cálculo da área²: altura x largura
area = a * l
# cálculo da tinta: 1L = 2m²
lt = area / 2
# quantidade de tinta:
print('considerando {}m² de parede, a quantidade necessária de tinta para pintá-la será de {}L'. format(area, lt))





