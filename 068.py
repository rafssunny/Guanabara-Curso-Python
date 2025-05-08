from random import randint
jogador = vitorias = 0
maquina = randint(1, 10)
escolha = ''
while True:
    escolha = str(input('escolha ímpar ou par'))
    jogador = int(input('Insira um valor de 1 a 10: '))
    print(f'Você jogou {jogador}, a máquina jogou {maquina}')
    jogador+=maquina
    if jogador %2 != 0 and escolha == 'par' or jogador %2 == 0 and escolha == 'impar':
        print('Você perdeu!')
        break
    else:
        jogador-=jogador
        print('Você ganhou, vamos prosseguir!')
        vitorias+=1
print(f'Obrigado por jogar, você ganhou {vitorias} vezes')