"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('AMOR', 'BAIXINHO', 'CARACOL', 'DOCINHO', 'ESCOLA',
            'FACA', 'GENTE', 'HUMANO', 'IGUALDADE', 'JUVENTUDE')
for _ in palavras:
    print(f' \nNa palavra {_} temos ', end=' ')
    for letra in _:
        if letra in 'AEIOU':
            print(letra, end=' ')
