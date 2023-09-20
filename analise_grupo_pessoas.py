"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo,
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos."""

maior_idade_h = 0
nome_h_velho = 0
m_menor_20 = 0
soma_idade = 0
media_idade = 0

for dados in range(1, 5):
    print('-' * 10, f'{dados}° Pessoa', '-' * 20)
    nome = str(input(f'Digite o nome da {dados}° pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {dados}° pessoa: '))
    sexo = int(input(f"""Digite o sexo da {dados}° pessoa:
    [ 1 ] Feminino
    [ 2 ] Masculino:  """))
    soma_idade += idade

    if sexo == 1 and idade < 20:
        m_menor_20 += 1

    if dados == 1 and sexo == 2:
        maior_idade_h = idade
        nome_h_velho = nome

    if sexo == 2 and idade > maior_idade_h:
        maior_idade_h = idade
        nome_h_velho = nome

media_idade = soma_idade / 4
print(f'A média da idade das pessoas nesse grupo é {media_idade} anos.')
print(f'O homem mais velho neste grupo tem {maior_idade_h} anos e se chama {nome_h_velho}.')
print(f'Neste grupo, têm {m_menor_20} mulheres com menos de 20 anos.')
