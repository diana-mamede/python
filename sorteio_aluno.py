# Um professor quer sortear um dos deus quatro alunos para apagar o quadro, faça um programa que leia o nome dos alunos e escreva o nome do escolhido.

import random
primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
segundo_aluno = str(input('Digite o nome do segundo aluno: '))
terceiro_aluno = str(input('Digite o nome do terceiro aluno: '))
quarto_aluno = str(input('Digite o nome do quarto aluno: '))
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
sorteio = random.choice(lista)
print(f'O aluno escolhido foi: {sorteio}!')
