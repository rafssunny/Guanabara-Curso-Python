futebol = dict()
gols = list()
total = 0
futebol['Jogador'] = str(input('Qual o nome do jogador?'))
futebol['Jogos'] = int(input('Quantos jogos ele jogou?'))
for c in range(0,futebol['Jogos']):
    gols.append(int(input(f'Quantos gols na partida {c}?')))
    if c == futebol['Jogos']-1:
        futebol['gols'] = gols[:]
        for tota in futebol['gols']:
            total+=tota
        futebol['Total'] = total
        del futebol['Jogos']
print('-='*20)
print(futebol)
print('-='*20)
for n, p in futebol.items():
    print(f'O campo {n} tem valor {p}')
print('-='*20)
print(f'O jogador {futebol['Jogador']} jogou {len(gols)} partidas.')
for pos, parti in enumerate(gols):
    print(f'{'=>':>5}', end = '')
    print(f'Na partida {pos} fez {parti} gols.')
print(f'Foi um total de {futebol['Total']} gols.')