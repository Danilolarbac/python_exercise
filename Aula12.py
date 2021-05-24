# Vamos analizar o uso da condicional elif para estruturas condicionais aninhadas

nome = str(input('Qual e o seu nome? '))
if nome == 'Danilo':
    print('Que nome bonito')
elif nome == 'Antony' or nome == 'Herika' or nome == 'Socorro':  # Estrutura condicional aninhada
    print('Seu nome e bem popular no Brasil.')
elif nome in 'Katia Lui Dena Marina Sandra':
    print('Belo nome feminino voçe tem')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia {}'.format(nome))
