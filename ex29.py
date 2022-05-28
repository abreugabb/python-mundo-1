'''
faça um programa que leia uma frase e mostre:
1. quantas vezes aparece a letra A
2. em que posição ela aparece a primeira vez
3. em que posição ela aparece a última vez
'''

frase = str(input('digite uma frase: ')).upper().strip() # usar funções na primeira linha pra facilitar o processo
print('a letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('a letra "A" aparece pela primeira vez na posição: {}'.format(frase.find('A')+1)) # usar +1 pra somar 1 à posição e deixar como primeiro caractere o nº 1
print('a letra "A" aparece pela última vez na posição: {}'.format(frase.rfind('A')+1))