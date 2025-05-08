from random import randint
numero = int(input('Joga da advinhação! Fale um número de 1 a 5: '))
escolha = randint(1, 5)
if numero == escolha:
    print(f'parabens voce ganhou, o número sorteado foi {escolha}')
else:
    print(f'é foda man, vc perdeu, o número escolhido foi {escolha}')