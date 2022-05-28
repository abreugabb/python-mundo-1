a = input('digite algo para informações: ')

print(' tipo primitivo de dado: ', type(a))
print(' é um número ou uma letra?', a.isalnum())
print(' é uma letra?', a.isalpha())
print(' é um número?', a.isnumeric())
print(' está digitado em letras maiúsculo?', a.isupper())
print(' está digitado em letras minúsculas?', a.islower())
print(' está capitalizada?', a.istitle())

