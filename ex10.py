# faça um programa que leia um número inteiro
# e mostre seu antecessor e o seu sucessor

n = int(input('digite um número: '))
ant = n - 1
suc = n + 1
# caso não haja necessidade de validar essa info novamente é só fazer o cálculo dentro de uma variável só
# ex.: print('número antecessor é {} e o sucessor é {}'.format(n-1), (n+1))
print('número antecessor é {} e o sucessor é {}'.format(ant, suc))