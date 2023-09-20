"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

maioridade = homem = mulher_menos_vinte = 0

while True:
    print('*' * 30)
    print('CADASTRE UMA PESSOA')
    print('*' * 30)
    idade = int(input(f'Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo [F/M]: ')).strip().upper()[0]

    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem +=1
    if idade < 20 and sexo == 'F':
        mulher_menos_vinte += 1

    continuar =int(input("""
    Deseja continuar?
    [ 0 ] Não
    [ 1 ] Sim
    """))
    if continuar == 0:
        break

print('=' * 30)
print(f"""
No grupo de pessoas citadas:
Há {maioridade} pessoas maiores de 18 anos.
Foram adicionados {homem} homens.
E {mulher_menos_vinte} mulheres com menos de 20 anos.
""")
print('=' * 30)
