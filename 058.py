from random import randint
numero = randint(0, 10)
tentativas = 0
resposta = int()
while resposta != numero:
    resposta = int(input('Advinhe o número que estou pensando '))
    print('Errado!')
    tentativas += 1
print(f'Parabéns, você acertou! o número era {numero} e foram necessárias {tentativas} tentativas para acertar')
