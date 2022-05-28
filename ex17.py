# faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

v = float(input('informe o valor do produto: R$'))
# cálculo do desconto
dc = v * 95 / 100
# preço com desconto aplicado
print('o valor do produto com desconto de 5% é de R${:.2f}'.format(dc))