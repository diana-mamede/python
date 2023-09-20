# Crie um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200 km e R$0,45 para viagens mais longas.

distancia = int(input('Qual a distância, em quilômetros, percorrida nessa viagem? '))
preco_viagem_curta = 0.5 * distancia
preco_viagem_longa = 0.45 * distancia
if distancia > 200:
    print(f'Para uma viagem de {distancia}km, o valor cobrado por passagem sera de R${preco_viagem_longa :.2f}. Obrigada e viaje com cuidado!')
else:
    print(f'Para uma viagem de {distancia}km, o valor cobrado por passagem será de R${preco_viagem_curta :.2f}. Obrigada e viaje com cuidado!')
