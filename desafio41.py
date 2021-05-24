# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua
# categoria, de acordo com a idade:
# - Até 9 anos: Mirin
# -Até 14 anos: Infantil
# -Até 19 anos: Junior
# -Até 20 anos: Sênior
# -Acima: Master

from datetime import date
data = int(input('Por favor digite o ano de seu nascimento: '))
idade = date.today().year - data
if idade <= 9:
    print('Você possui {} anos por isso sua categoria é \033[1;31mMirim\033[m'.format(idade))
elif 9 < idade <= 14:
    print('Você possui {} anos por isso sua categoria é \033[1;36mInfantil\033[m'.format(idade))
elif 14 < idade <= 19:
    print('Você possui {} anos e por isso sua categoria é \033[1;32mjunior\033[m'.format(idade))
elif 19 < idade <= 25:
    print('Você possui {} anos e por isso sua categoria é \033[1;33mSênior\033[m'.format(idade))
else:
    print('Você possui {} anos e por isso sua categoria é \033[1;31mMaster\033[m'.format(idade))
