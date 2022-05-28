'''
desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

condição: se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
'''

l1 = int(input('informe o comprimento da primeira reta: '))
l2 = int(input('informe o comprimento da segunda reta: '))
l3 = int(input('informe o comprimento da terceira reta: '))

soma = l1 + l2
if soma > l3:
    print('pode formar um triângulo!')
else:
    print('não pode formar um triângulo!')


a = 19 % 2
print(a)