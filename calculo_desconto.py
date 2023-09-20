# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_atual = float(input('Preço atual do produto: R$'))
desconto = preco_atual*5/100
preco_final = preco_atual - desconto
print(f'Com desconto de 5%, o produto sairá por: R${preco_final :.2f}')
