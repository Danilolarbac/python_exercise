# Cores no terminal
nome = 'Danilo'
cores = {'limpa': '\033[m',
         'azul': '\033[m34',
         'amarelo': '\033[33m',
         'pretoebranco' : '\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!!! '.format(cores['amarelo'], nome, cores['limpa']))
# print('Olá, muito prazer em te conhecer, {}{}{}!!!! '.format('\033[4;34m', nome, '\033[m'))
