"""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, segundo a média:
- Media abaixo de 5.0 = REPROVADO
- Media entre 5.0 e 6.9 = RECUPERACAO
- Media 7.0 ou superior = APROVADO"""

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
media = (nota_um + nota_dois) / 2
if media < 5.0:
    print(f'Sua média final é: {media :.1f} REPROVADO(A).')
elif 5.0 <= media < 6.9:
    print(f'Sua média final é: {media :.1f} RECUPERAÇÃO.')
elif media >= 7.0:
    print(f'Sua média final é: {media :.1f} APROVADO(A).')
