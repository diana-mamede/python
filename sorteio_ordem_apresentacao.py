# Um professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
primeiro_aluno = str(input('Nome do primeiro aluno: '))
segundo_aluno = str(input('Nome do segundo aluno: '))
terceiro_aluno = str(input('Nome do terceiro aluno: '))
quarto_aluno = str(input('Nome do quarto aluno: '))
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(lista)
print(f'A ordem de apresentação será: ')
print(lista)
