# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a
# tabela abaixo:
# -Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 ate 30: Sobrepeso
# - 30 a 40: Obesidade
# - Acima de 40: Obesidade morbida

print('-=-'*14)
print('CALCÚL0 DO ÍNDICE DE MASSA CORPORAL (IMC)')
print('-=-'*14)
peso = float(input('Digite o valor de seu peso Kg: '))
altura = float(input('Digite o valor de sua altura m: '))
imc = peso/pow(altura, 2)  # Imc kg/m²
print('Sei Imc e {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc <= 25:
    print('Parabéns! Você esta no peso ideal')
elif 25 < imc <= 30:
    print('Cuidado! Você está com sobrepeso')
elif 30 < imc <= 40:
    print('Atenção! Você está com obesidade')
else:
    print('Perigo! Você está com obesidade morbida, procure um médico')
