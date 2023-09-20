"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Bahia."""

colocados = ('Botafogo', 'Flamengo', 'Palmeiras', 'Gremio', 'Fluminense',
             'Red Bull Bragantino', 'Athletico', 'Sao Paulo', 'Cuiaba', 'Cruzeiro',
             'Fortaleza', 'Internacional', 'Atletico', 'Corinthians', 'Santos',
             'Goias', 'Bahia', 'Coritiba', 'America', 'Vasco')
print('=' * 30)
print(f'Lista de colocados no Brasileirão: {colocados}')
print('=' * 30)
print(f'Os 5 primeiros colocados do Campeonato foram: {colocados[0:5]}')
print('=' * 30)
print(f'Os 4 últimos colocados foram: {colocados[-4:]}')
print('=' * 30)
print(f'Os times colocados entre os 20 melhores, em ordem alfabética: {sorted(colocados)}')
print('=' * 30)
print(f'O Bahia está na {colocados.index("Bahia")+1}° posição.')
