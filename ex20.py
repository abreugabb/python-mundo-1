'''faça um programa que leia o comprimento do cateto oposto e adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa
dica: módulo .math

cateto oposto: em frente ao ângulo (vertical)
cateto adjacente: ao lado do ângulo (horizontal)
a soma dos quadrados dos catetos é igual o quadrado da hipotenusa'''

import math
# ou from math import hypot
co = float(input('informe o cateto oposto: '))
ca = float(input('informe o cateto adjacente: '))
# cálculo da hipotenusa por meio da matemática
h =(ca**2 + co**2) ** (1/2)
    # cálculo da hipotenusa por meio da função
            #h = math.hypot(co,ca)
# resultado
print('o comprimento da hipotenusa é {:.2f}'.format(h))


