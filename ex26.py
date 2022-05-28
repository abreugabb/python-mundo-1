'''
faça um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos separados
ex.: digite um número: 1834
  unidade: 4
  dezena: 3
  centena: 8
  milhar: 1
obs.: tentar como string e matematicamente
'''

#resolução por string
n = str(input('digite um número de quatro dígitos: ')) #para fazer de 0 a 9999 precisa de if
#função para adicionar espaços no entre cada número
nd = n.replace('',' ')
# função para transformar os números em uma lista
nd = nd.split()
# resultados em ordem decrescente
print('  unidade: {}'.format(nd[3]))
print('  dezena:  {}'.format(nd[2]))
print('  centena: {}'.format(nd[1]))
print('  milhar:  {}'.format(nd[0]))


# resolução matemática:
n = int(input('digite um número de quatro dígitos: '))
un = n % 10 # pega o resto da divisão por 10 e coloca na variável
x = n // 10 # divide por 10 para obter o resultado da próxima divisão
dz = x % 10
y = x // 10
ct = y % 10
z = y // 10
ml = z % 10

print('  unidade: {}'.format(un))
print('  dezena:  {}'.format(dz))
print('  centena: {}'.format(ct))
print('  milhar:  {}'.format(ml))

