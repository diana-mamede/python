# Quantas letras tem o primeiro nome

nome_completo = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Em maiúsculas:', nome_completo.upper())
print('Em minusculas: ', nome_completo.lower())
print('Quantidade de letras: ', len(nome_completo)-nome_completo.count(' '))
print('Primeiro nome tem essa quantidade de letras: ', nome_completo.find(' '))
