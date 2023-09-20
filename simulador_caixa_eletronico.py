"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('=' * 30)
print('CAIXA ELETRÔNICO')
print('=' * 30)

valor_saque = int(input('Quanto você gostaria de sacar: R$ '))
montante = valor_saque
cedula_atual = 50
total_cedula = 0
print(f'O valor de R${valor_saque :.2f} será pago em')
while True:
    if montante >= cedula_atual:
        montante -= cedula_atual
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'{total_cedula} de R${cedula_atual :.2f}')
        if cedula_atual == 50:
            cedula_atual = 20
            total_cedula = 0
        elif cedula_atual == 20:
            cedula_atual = 10
            total_cedula = 0
        elif cedula_atual == 10:
            cedula_atual = 1
            total_cedula = 0
        if montante == 0:
            break

print('=' * 30)
print('Volte sempre! Tenha um ótimo dia!')
print('=' * 30)
