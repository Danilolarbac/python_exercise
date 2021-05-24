# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
# le-se cidade[:5].capitalize() == 'Santo'  --> se a cidade e igual == a 'Santo'

cidade = str(input('Informe o nome de sua cidade: ')).strip()
dividido = cidade.split()
print('Santo' in dividido[0].capitalize())

#print(cidade[:5].capitalize() == 'Santo')

#dividido = cidade.split()
#print('O nome de sua cidade e {} \nSeu primeiro nome e {} \nE ela {} começa com Santo'.format(cidade, dividido[0],
#'Santo' in dividido[0].capitalize()))
