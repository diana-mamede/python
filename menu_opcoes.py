"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do Programa"""

primeiro_valor = float(input('Digite o primeiro valor: '))
segundo_valor = float(input('Digite o segundo valor: '))
opcao = int(input("""Menu
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa \n
"""))

while opcao != 5:
    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma de {primeiro_valor} + {segundo_valor} é {soma}')
        opcao = int(input("""Menu
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa \n
        """))

    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} resulta em {multiplicacao}')
        opcao = int(input("""Menu
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa \n
        """))

    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O primeiro valor inserido é maior!')
        elif segundo_valor > primeiro_valor:
            print(f'O segundo valor inserido é maior!')
        elif primeiro_valor == segundo_valor:
            print('Os dois valores digitados são iguais!')
        opcao = int(input("""Menu
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa \n
        """))

    elif opcao == 4:
        primeiro_valor = float(input('Digite um valor: '))
        segundo_valor = float(input('Digite um valor: '))
        opcao = int(input("""Menu
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa \n
        """))

    else:
        print('Opção Invalida. Tente novamente!')
        opcao = int(input("""Menu
                [ 1 ] Somar
                [ 2 ] Multiplicar
                [ 3 ] Maior
                [ 4 ] Novos números
                [ 5 ] Sair do programa \n
                """))

print('Fim do programa. Volte sempre!')
