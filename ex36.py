'''
faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
n1 = int(input('informe um número: '))
n2 = int(input('informe outro número: '))
n3 = int(input('informe mais um número: '))


if n1 > n2 and n1 > n3:
    print("o maior número é: {}".format(n1))
elif n2 > n1 and n2 > n3:
    print('o maior número é: {}'.format(n2))
elif n3 > n1 and n3 > n2:
    print('o maior número é: {}'.format(n3))
print("-" * 20)
if n1 < n2 and n1 < n3:
    print('o menor número é: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('o menor número é: {}'.format(n2))
elif n3 < n1 and n3 < n2:
    print('o menor número é: {}'.format(n3))

'''
também é possível fazer a verificação considerando por exemplo:
menor = a
if b < a and b < c
menor = b
if c < a and c < b
menor = c
isso elimina um if e torna o código mais enxuto 
'''