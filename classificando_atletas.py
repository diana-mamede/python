"""A Confederação Nacional de Natação precisa de um programa que leia a idade de um atleta e mostre sua categoria:
- Até 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Ate 19 anos: JUNIOR
- Ate 20 anos: SENIOR
- Acima: MASTER"""

idade = int(input('Digite a idade do participante: '))
if idade < 9:
    print(f'Com {idade} anos, a categoria de participação é MIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos, a categoria de participação é INFANTIL.')
elif idade <= 19:
    print(f'Com {idade} anos, a categoria de participação é JUNIOR.')
elif idade <= 25:
    print(f'Com {idade} anos, a categoria de participação é SENIOR.')
elif idade > 25:
    print(f'Com {idade} anos, a categoria de participação é MASTER.')
