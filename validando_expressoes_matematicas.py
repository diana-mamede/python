"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Ele deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressao = str(input('Digite uma expressão matemática: '))
lista = []

for caractere in expressao:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Os parenteses estão empregados corretamente.')
else:
    print('O uso dos parenteses está incorreto.')
