# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e quantos dias de aluguel. Calcule o preço a pagar, sabendo que: R$60,00 por dia e R$0,15 por km.

dias_aluguel = int(input('Por quantos dias o carro foi alugado?'))
km_rodados = float(input('Quantos quilômetros foram percorridos?'))
preco = (60*dias_aluguel) + km_rodados*0.15
print(f'O valor total a ser pago pelo aluguel é de R${preco :.2f}.')
