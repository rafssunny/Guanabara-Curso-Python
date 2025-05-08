from random import sample
from time import sleep
print('-'*20)
print(f'{'JOGA NA MEGA SENA':^20}')
print('-'*20)
quantidade = int(input('Quantos jogos você quer que eu sorteie?'))
dados_secundarios = list()
dados_principais = list()
contagem = 0
while contagem != quantidade:
    numeros = list(range(1,61))
    dados_principais.append(sample(numeros[:], 6))
    dados_secundarios.append(dados_principais[:])
    dados_principais.clear()
    contagem+=1
print(f'-=-=-= SORTEANDO {quantidade} JOGOS -=-=-= ')
for dados in range(0,quantidade):
    print(f'Jogo {dados+1}: {sorted(dados_secundarios[dados][0])}')
    sleep(1)