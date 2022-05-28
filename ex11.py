# crie um algoritmo que leia um nº e mostre seu dobro, triplo e raiz quadrada

n = int(input("digite um número: "))
db = n * 2
tp = n * 3
rq = n ** (1/2) #ou por meio da função pow >> pow(n, (1/2)
print('o dobro do número digitado é {} \no triplo é {} \ne sua raiz quadrada é {:.2f}'.format(db, tp, rq))