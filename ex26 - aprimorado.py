'''
faça um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos separados
ex.: digite um número: 1834
  unidade: 4
  dezena: 3
  centena: 8
  milhar: 1
obs.: tentar como string e matematicamente
'''

# maneira mil vezes mais simples de resolver:

# para fazer de 0 a 9999 precisa de if
num = int(input('digite um número de quatro dígitos: '))
n = str(num)
# aqui ele vai buscar o número por meio do fatiamento da string
print('  unidade: {}'.format(n[3]))
print('  dezena:  {}'.format(n[2]))
print('  centena: {}'.format(n[1]))
print('  milhar:  {}'.format(n[0]))

# resolução matemática:

# funciona de 0 a 9999
num = int(input('digite um número de quatro dígitos: \n'))
# cálculo simplificado
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('  unidade: {}'.format(u))
print('  dezena:  {}'.format(d))
print('  centena: {}'.format(c))
print('  milhar:  {}'.format(m))

