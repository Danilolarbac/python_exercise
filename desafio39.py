# Faça um progama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar.
# - Se ja passou do tempo de alistamento.
# Seu programa tambem deverá mostar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Digite o ano de nascimento: '))
sexo = str(input('Qual o seu genero: ')).strip().capitalize()
atual = date.today().year  # importa o ano atual da maquina
idade = atual - ano

if sexo == 'Masculino':
    if idade < 18:
        print('Você não tem idade para se alistar, sua idade e {} e ainda faltam {} anos'.format(idade, 18 - idade))
        print('Seu alistamento e em {} ano'.format(atual + (18 - idade)))
    if idade == 18:
        print('\033[1;33mParabés!\033[m voce tem {} anos é esta apto para o alistamento militar'.format(idade))
    if idade > 18:
        print('\033[1;31mAtenção!\033[m, você passou {} anos do prazo para o alistamento militar. '.format(idade - 18),
          end='')
        print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
        print('Procure a junta militar mais proxima para regularizar sua situação')
elif sexo == 'Feminino':
    print('Seu sexo e Feminino você não e obrigada a se alistar')
