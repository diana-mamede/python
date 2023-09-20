""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente."""
ficha = []

while True:
    nome = str(input('Nome: '))
    primeira_nota = float(input('Nota 1: '))
    segunda_nota = float(input('Nota 2: '))
    media = (primeira_nota + segunda_nota) / 2
    ficha.append([nome, [primeira_nota, segunda_nota], media])
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta in 'N':
        break

print(f'{"N°":<5}{"NOME":<10}{"MÉDIA":>10}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<5}{aluno[0]:<10}{aluno[2]:>10.1f}')

while True:
    opcao = int(input('Mostrar notas individuais de qual aluno? [999 para parar]: '))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
