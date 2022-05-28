# crie um programa que leia quantos reais uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar (considere US$1.00 = R$3.27)

r = float(input('digite o valor em reais: '))
dol = r / 3.27
print('com R${} você pode comprar US${:.2f}'.format(r, dol))