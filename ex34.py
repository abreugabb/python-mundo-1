'''
desenvolva um programa que pergunte a distância de uma viagem em Km.
calcule e peça o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

km = float(input('\033[1;32minforme a distância em km: '))
if km <= 200:
    p = km * 0.50
    print('\033[1;36mo valor da passagem será de: R${:.2f}'.format(p))
else:
    p = km * 0.45
    print('\033[1;34mo valor da passagem será de: R${:.2f}'.format(p))