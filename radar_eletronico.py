# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7.00 por cada km acima do limite.

velocidade = int(input('Qual a velocidade do carro? '))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print(f'Calma no volante! Você foi multado. O custo da multa é de R${multa :.2f}')
else:
    print('Continue assim! Dirija sempre com segurança!')
