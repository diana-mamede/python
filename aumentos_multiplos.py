# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

salario_inicial = float(input('Qual o seu salário, em reais, atualmente: '))
salario_minimo = salario_inicial + (salario_inicial*15/100)
salario_maior = salario_inicial + (salario_inicial*10/100)
if salario_inicial > 1250.00:
    print(f'Com o aumento de 10%, seu novo salário será: R${salario_maior :.2f}')
else:
    print(f'Com o aumento de 15%, seu novo salário será: R${salario_minimo :.2f}')
