# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome, separadamente.

nome_completo = input('Digite seu nome completo: ').strip().split()
print('Opa, prazer em te conhecer!')
print('O primeiro nome é: ', nome_completo[0])
print('O ultimo nome é: ', nome_completo[-1])
