# Escreva um programa que pergunte qual o salario de um funcionario e calcule o valor de seu aumento. Para salarios
# superiores a R$1.250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário? R$ '))
if salario >= 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
print('De acordo com o seu salário de {}R$ você receberá um reajuste de {}R$ e seu novo salário será {}R$'
      .format(salario, aumento, salario + aumento))
