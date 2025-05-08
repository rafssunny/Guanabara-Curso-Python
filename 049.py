print(20*'='+'TABUADA'+20*'=')
x = int(input('insira o numero que voce quer ver a tabuada: '))
for tabuada in range(1, 11):
    print(f'{x}*{tabuada} = {x*tabuada}')