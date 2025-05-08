from random import choice
from time import sleep
print('JOKENPO')
escolhas = 'pedra', 'papel', 'tesoura'
maquina = choice(escolhas)
jogador = str(input('Escolha o que voce quer jogar(pedra, papel ou tesoura): '))
jogador = jogador.lower().strip()
print('Robô escolhendo a jogada...')
sleep(2)
if maquina == 'pedra' and jogador == 'tesoura' or maquina == 'tesoura' and jogador == 'papel' or maquina == 'papel' and jogador == 'pedra':
    print(f'Você perdeu! O Robô jogou {maquina} e você {jogador}. Mais sorte da próxima!')
elif jogador == 'pedra' and maquina == 'tesoura' or jogador =='tesoura' and maquina == 'papel' or jogador == 'papel' and maquina == 'pedra':
    print(f'Você ganhou! O Robô jogou {maquina} e você {jogador}. Parabéns!')
else:
    print(f'Puts! foi empate, o Robô jogou {maquina} e você {jogador}.')
print('Obrigado por jogar!')