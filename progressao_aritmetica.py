# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=' * 20)
print('10 TERMOS DE UMA P.A.')
print('=' * 20)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for pa in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{pa} ⇢ ', end=' ')
print('FIM.')
