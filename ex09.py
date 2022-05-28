n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
# realizar cálculo dentro do parenteses
print('a soma entre os números é {}'.format(n1+n2))
# realizar cáculos com variaveis declaradas
sm = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
pt = n1 ** n2
md = n1 % n2
# mostrar resultados
print('a soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3}'.format(sm, sb, m, d), end=' ') # end= serve pra cancelar a quebra de linha (pode adicionar coisas dps do =)
print('a divisão inteira é {}, a potência é {} e o módulo é {}'.format(di, pt, md))
