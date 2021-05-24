# Faça um algoritimo que leia o salário de um funcionario e mostre seu novo salairo. Com um aumento de 15%.

s = float(input('Informe o seu salário: R$  '))
print('Seu salário é {:.2f} R$ com um aumento de 15% seu novo salário é {:.2f} R$'.format(s, s + (s * 0.15)))
