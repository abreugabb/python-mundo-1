'''faça um programa que leia um ângulo qualquer e
mostre o valor do seno, cosseno e tangente desse ângulo'''

import math

ang = int(input('digite um ângulo qualquer em graus: '))
# função que converte graus em radianos
rad = math.radians(ang)
# resultado: função lê o número em radianos
print('o seno é: {:.3f}'.format(math.sin(rad)))
print('o cosseno é: {:.3f}'.format(math.cos(rad)))
print('a tangente é: {:.3f}'.format(math.tan(rad)))
