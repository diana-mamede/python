"""Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

print('*' * 20)
print('COMPRAS!')
print('*' * 20)

soma = mais_mil_reais = menor_preco = contagem = 0
produto_mais_barato = ' '

while True:
    nome_produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    valor_produto = float(input('Digite o valor do produto: R$ '))
    soma += valor_produto
    contagem += 1

    if contagem == 1 or valor_produto < menor_preco:
        menor_preco = valor_produto
        produto_mais_barato = nome_produto

    if valor_produto > 1000:
        mais_mil_reais += 1

    continuar =int(input("""
        Deseja continuar?
        [ 0 ] Não
        [ 1 ] Sim
        """))

    if continuar == 0:
        break

print(f"""
Total Gasto: R$ {soma :.2f}
Quantidade de produtos que custam + 1mil reais: {mais_mil_reais}
O produto mais barato foi {produto_mais_barato}, que custa R${menor_preco :.2f}.
Obrigada! Volte sempre.
""")
