''' crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome '''

nome = str(input('digite seu nome completo: ')).title()
print('seu nome contém o sobrenome Silva?: {}'.format('Silva' in nome))