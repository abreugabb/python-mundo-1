'''programa que leia um número real qualquer e mostre na tela sua porção inteira
ex.: digite um número: 6.127
o número 6.127 tem parte inteira 6
dica: olhar funções do módulo .math'''

 forma 1: usando o módulo completo
 #import math
forma 2: usando apenas a função específica
from math import trunc

n = float(input('digite um número real: '))
pt = trunc(n) # retorna n com a parte fracionária removida, deixando somente a parte inteira
# é possível resolver sem importação, apenas usando a função int || ex.: pt = int(n)
print('o número {} tem parte inteira {}'.format(n, pt))