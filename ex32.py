'''
escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7,00 por cada Km acima do limite.
'''

vl = int(input('informe a velocidade do carro: '))
if vl > 80:
    print('você foi multado por ultrapassar o limite de velocidade!')
    multa = (vl - 80) * 7.00 # calcular apenas o valor excedente
    print('valor da multa: R${:.2f}'.format(multa))
else:
    print('você está dentro do limite de velocidade, tenha um bom dia!')