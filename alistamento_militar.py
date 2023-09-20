""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se ja passou o tempo do alistamento
O programa tambem devera mostrar o tempo que falta ou que passou do prazo."""

import datetime
ano_nascimento = int(input('Digite a seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f'Como você já tem {idade} anos, já está na hora de se apresentar ao exercito.')
elif idade > 18:
    print(f'Você já tem {idade} anos, já passou da hora de se apresentar. O prazo foi a {idade - 18} anos.')
elif idade < 18:
    print(f'Você ainda tem {idade} anos, sua apresentação ao exercito será daqui a {18 - idade} anos.')
