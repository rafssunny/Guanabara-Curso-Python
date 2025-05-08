print('Progressão aritmética')
razao = int(input('Insira a razão dessa progressão:'))
primeiro = int(input('Insira o primeiro termo dessa progressão'))
for progressao in range(primeiro, primeiro+((11-1)*razao), razao):
    print(progressao)