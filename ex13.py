# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

# tabela de conversão: km | hm | dam | m | dm | cm | mm
m = float(input('digite o valor em metros: '))
# converter metros pra km dividir por 1000
km = m / 1000
# converter metros pra hm dividir por 100
hm = m / 100
# converter metros pra km dividir por 10
dam = m / 10
# converter metros pra dm multiplicar por 100
dm = m * 10
# converter metros pra cm multiplicar por 100
cm = m * 1001
# converter metros pra mm multiplicar por 1000
mm = m * 1000
# converter metros pra cm multiplicar por 1000
print('km | hm | dam | m | dm | cm | mm')
print('{} | {} | {} | {} | {} | {} | {}'.format(km, hm, dam, m, dm, cm, mm))