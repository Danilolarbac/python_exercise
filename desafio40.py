# Crie um programa que leia duas notas de um aluno be calcule sua média, mostrando uma mensagem no final, de acordo com
# a media atingida:
# - Média baixo de 5.0 Reprovado
# - Média entre 5.0 e 6.9 Recuperação
# - Média 7.0 ou superior Aprovado

print('-=-'*10)
print('\033[1;4;33mCálculo da média\033[m')
print('-=-'*10)
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('\033[1;34mParabens!\033[m sua média foi {:.1f} e você foi Aprovado'.format(media))
elif 7 > media >= 5:
    print('\033[1;31mAtenção!\033[m sua média foi {:.1f} você está na recuperação'.format(media))
else:
    print('\033[1;31mAtenção!\033[m sua média foi {:.1f} você esta reprovado'.format(media))
