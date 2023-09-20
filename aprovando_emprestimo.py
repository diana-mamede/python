""" Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
Calcule o valor da pretacao mensal, nao pode exceder 30% do salario ou emprestimo negado."""

valor_casa = float(input('Qual o valor, em reais, da casa que você pretende comprar? '))
salario = float(input('Qual o seu salário atual?'))
anos_pagamento = float(input('Em quantos anos você vai pagar? '))
prestacao_mensal = valor_casa / (anos_pagamento * 12)

if prestacao_mensal > (salario * 30 / 100):
    print('Sinto muito! Não será possível prosseguir com seu emprestimo.')
else:
    print(f'Tudo certo! O emprestimo pode ser concedido. Sua parcela será de R${prestacao_mensal :.2f} mensais. \n Totalizando {valor_casa}, dividido em {anos_pagamento} anos. Obrigada pela preferência! ')
