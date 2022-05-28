# prof quer sortear um dos quatro alunos para apagar o quadro.
# crie programa que leia o nome deles e escreva o nome escolhido

import random
# from random import choice

a1 = (input('nome do aluno(a) 1: '))
a2 = (input('nome do aluno(a) 2: '))
a3 = (input('nome do aluno(a) 3: '))
a4 = (input('nome do aluno(a) 4: '))

print('aluno sorteado para apagar o quadro foi: {}'.format(random.choice([a1, a2, a3, a4])))
