"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
import datetime

ano_atual = datetime.date.today().year
maior_idade = 0
menor_idade = 0

for x in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento {x}° da pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior_idade += 1
    elif idade < 18:
        menor_idade += 1

print(f'Nessa lista, existem {maior_idade} pessoas maiores de idade')
print(f'E {menor_idade} pessoas menores de idade')
