# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite um ano para descobrir se ele é bissexto \nou digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'Sim! {ano} é um ano bissexto.')
else:
    print(f'Não! {ano} não é um ano bissexto.')
