from random import randint
from time import sleep
dados = {'Jogador1': randint(1,6), 'Jogador2': randint(1,6), 'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)
         }
cont = 1
print(f'Jogador 1 tirou {dados['Jogador1']}')
sleep(1)
print(f'Jogador 2 tirou {dados['Jogador2']}')
sleep(1)
print(f'Jogador 3 tirou {dados['Jogador3']}')
sleep(1)
print(f'Jogador 4 tirou {dados['Jogador4']}')
sleep(1)
print('Ranking dos Jogadores: ')
sorteado = dict(sorted(dados.items(), key = lambda item:item[1], reverse=True))
for c, n in sorteado.items():
    print(f'{cont}° Lugar: {c} com {n}')
    sleep(1)
    cont+=1
