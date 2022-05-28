'''
escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
para salários superiores a R$1.250,00, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento é de 15%.
'''

slr = float(input('informe seu salário: R$'))

if slr > 1250.00:
    aum = slr * 1.1
    print('\033[1;36mparabéns!\033[m\nvocê recebeu um aumento de \033[1;35m10%\033[m sobre seu salário, o novo valor é de: \033[1;35mR${:.2f}\033[m'.format(aum))
else:
    aum = slr * 1.15
    print('\033[1;36mparabéns!\033[m\nvocê recebeu um aumento de \033[1;35m15%\033[m sobre seu salário, o novo valor é de: \033[1;35mR${:.2f}'.format(aum))