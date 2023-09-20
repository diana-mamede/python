""" Escreva um programa que leia dois numeros inteiros e compare-os.
Mostrando na tela uma dessas mensagens:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais."""

primeiro_numero = int(input('Digite um número inteiro: '))
segundo_numero = int(input('Digite outro numero inteiro: '))

if primeiro_numero > segundo_numero:
    print('O primeiro valor é maior.')
elif segundo_numero > primeiro_numero:
    print('O segundo valor é maior.')
elif primeiro_numero == segundo_numero:
    print('Os dois valores digitados são iguais.')
