# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

x = float(input('Insira o valor em metros: '))
print('O valor em decâmetro e {} \nO valor em hectômetro e {} \nO valor em quilômetro e {}'.format((x / 10), (x / 100), (x / 1000)))
print('O valor em centímetros e: {} cm \nO valor em decímetro e: {} \nO valor em milímetro e: {} mm '.format((x * 100), (x * 10), (x * 1000)))
