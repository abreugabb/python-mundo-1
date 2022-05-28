'''
escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário descobrir qual foi o número escolhido pelo computador.
o programa deverá escrever na tela se o usúario venceu ou perdeu.
'''

import random

num = random.randint(0, 5) # comando que faz o computador "pensar" em um inteiro entre 0 e 5
print("--" * 35)
n = int(input('descubra qual número eu estou pensando... escolha um número de 0 a 5: '))
print("--" * 35)
if n == num:
    print('parabéns! você venceu')
else:
    print('ah que pena! você perdeu\no número que o computador pensou foi {}'.format(num))