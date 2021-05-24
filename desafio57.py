# Faça um programa que leia o sexo de uma pessoa mas so aceite os valores M ou F caso esteja errado peça para digitar
# novamente ate ter um valor correto

sexo = str(input('Digite o seu genero[M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, digite novamente [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucessor'.format(sexo))
