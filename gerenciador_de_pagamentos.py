"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o preco normal e condicao de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou + no cartao: 20% juros"""

valor_produto = float(input('Digite o valor do produto, em reais: '))
forma_pagamento = float(input("""Escolha a forma de pagamento:
[ 1 ] = Dinheiro/Cheque
[ 2 ] = Cartão Debito
[ 3 ] = Cartao Credito até 2x
[ 4 ] = Cartão Credito + 2x:
"""))

if forma_pagamento == 1:
    print(f'O novo valor do produto, com 10% de desconto, será de R${valor_produto - (valor_produto*10/100) :.2f}. ')
elif forma_pagamento == 2:
    print(f'O novo valor do produto, com 5% de desconto, será de R${valor_produto - (valor_produto*5/100) :.2f}. ')
elif forma_pagamento == 3:
    print('O valor do produto não será alternado nesta forma de pagamento.')
elif forma_pagamento == 4:
    print(f'O novo valor do produto, com 20% de acréscimo, será de R${valor_produto + (valor_produto*20/100) :.2f}. ')
else:
    print('Opção INVALIDA de forma de pagamento.')
