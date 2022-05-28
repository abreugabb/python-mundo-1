''' faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente'''

# funções para: tornar a inicial Maiúscula + remover espaços inúteis + transformar em lista
nome = str(input('digite seu nome completo: ')).title().strip().split()
# escolher o último nome da lista
ult = nome[-1]
print('olá {} {}!'.format(nome[0], ult))
print('primeiro nome: {}'.format(nome[0]))
print('último nome: {}'.format(ult)) # ou format.[len(nome)-1]))