"""Melhore o df 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

print('=' * 20)
print('10 TERMOS DE UMA P.A.')
print('=' * 20)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
contagem = 1
total = 0
termo_mais = 10

while termo_mais != 0:
    total += termo_mais
    while contagem <= total:
        print(f'{termo} ⇢ ', end=' ')
        termo += razao
        contagem += 1
    print('PAUSA')
    termo_mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos.')
print('\nFim do programa.')
