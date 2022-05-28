# faça um programa que leia o salário e mostre seu novo salário, com 15% de aumento

s = float(input('digite seu salário atual: R$'))
ns = s * 1.15
# para reduzir casas decimais "flutuantes" usar {:.Nf}
print('o seu novo salário com 15% de aumento é de {:.2f}'.format(ns))