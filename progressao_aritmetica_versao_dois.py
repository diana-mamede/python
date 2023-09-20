# Refaça o df 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 20)
print('10 TERMOS DE UMA P.A.')
print('=' * 20)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
contagem = 1

while contagem <= 10:
    print(f'{termo} ⇢ ', end=' ')
    termo += razao
    contagem += 1

print('\nFim do programa.')
