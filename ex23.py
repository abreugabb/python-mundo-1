# prof quer sortear a ordem de apresentação dos alunos.
# crie programa que leia o nome deles e mostre a ordem sorteada

from random import shuffle

a1 = (input('nome do aluno(a) 1: '))
a2 = (input('nome do aluno(a) 2: '))
a3 = (input('nome do aluno(a) 3: '))
a4 = (input('nome do aluno(a) 4: '))
# variável para incluir alunos na lista
ordem = [a1, a2, a3, a4]
# função que embaralha os nomes inseridos na lista
shuffle(ordem)
print('a ordem sorteada para apresentação foi: ')
#queria deixar organizadinho em lista mas não to conseguindo
print (ordem)
