''' crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" '''

cid = str(input('digite o nome de uma cidade: ')).strip()
# função pra deixar a primeira letra maiúscula
cid = cid.capitalize()
print('cidade começa com o nome Santo?: {} '.format('Santo' in cid))