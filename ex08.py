nome = input('qual seu nome? ')
print('olá {}, prazer em te conhecer!'.format(nome))
# escrever variável em uma quantidade X de caracteres
print('olá {:20}, prazer em te conhecer!'.format(nome))
# escrever variável alinhando à esquerda em X caracteres
print('olá {:20}, prazer em te conhecer!'.format(nome))
# escrever variável alinhando à direita em X caracteres
print('olá {:>20}, prazer em te conhecer!'.format(nome))
# escrever variável centralizando em X caracteres
print('olá {:^20}, prazer em te conhecer!'.format(nome))
# escrever variável centralizando em X caracteres, com adição de sinal
print('olá {:=^20}, prazer em te conhecer!'.format(nome))
