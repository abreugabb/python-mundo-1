""" crie um programa que leia o nome completo de uma pessoa e mostre:
1. o nome com todas as letras maiúsculas
2. o nome com todas as minúsculas
3. quantas letras tem no total (desconsiderando espaços)
4. quantas letras tem o primeiro nome
gabriela abreu silva """

# pode-se usar strip na primeira variável desde que declare que é uma str
nome = str(input('informe seu nome completo: ').strip())
# quando eu coloco split para eliminar os espaços ele buga o minusculo e o maiusculo
print('nome escrito com todas letras maiúsculas: {}'.format(nome.upper()))
print('nome escrito com todas letras minúsculas: {}'.format(nome.lower()))
# função replace para tirar os espaços entre os nomes e calcular com len apenas as letras
print('total de letras do nome: {} '.format((len(nome.replace(' ',''))))) # ou usando .format(len(nome) - nome.count(' '))) >> vai contar os espaços e subtraí-los
# transformando o nome em lista para calcular apenas o primeiro
pn = nome.split()
print('total de letras do primeiro nome: {}'.format(len(pn[0])))
# ou .format(nome.find(' '))) >> vai encontrar o primeiro espaço e informar onde ele começa (ou seja, a quantidade de caracteres que o nome possui)
