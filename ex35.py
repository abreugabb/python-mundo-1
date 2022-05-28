'''
faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

confirmações:
- ser divisivel por 4
>> O ano é bissexto quando é divisível por 4, mas não por 100.
- ser divisivel por 100
>> O ano não é bissexto quando é divisível por 100, mas não por 400.
- ser divisel por 400

Caso 1) É um número divisível por 4, mas não é divisível por 100.
Caso 2) É um número divisível por 4, por 100 e por 400.
'''

from datetime import date

print('\033[1;34manalise aqui se um ano é ou não bissexto.')
ano = int(input('informe um ano qualquer ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('\033[33mo ano {} é bissexto'.format(ano))
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('\033[31mo ano {} não é bissexto'.format(ano))