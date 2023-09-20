# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = float(input('Digite seu salario atual: R$'))
aumento = salario_atual*15/100
salario_novo = salario_atual + aumento
print(f'Com o aumento de 15%, seu salário passará de R${salario_atual :.2f} para R${salario_novo :.2f}.')
