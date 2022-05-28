# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
# não esquecer da ordem de precedência dos cálculos
# se digitar media = n1 + n2 / 2 >> o programa vai entender que é pra dividir n2 / 2 e depois somar com n1
media = (n1 + n2) / 2
print('média final das notas: {}'.format(media))
