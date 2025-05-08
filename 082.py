valores = []
pares = []
impares = []
cont = 0
pergunta = ''
while True:
    valores.append(int(input('Insira um valor: ')))
    pergunta = str(input('Quer continuar?sim/nao'))
    if pergunta == 'nao':
        break
for pos, c in enumerate(valores):
    if valores[pos] % 2 == 0:
        pares.append(valores[pos])
    else:
        impares.append(valores[pos])
print(f'A lista gerada foi {valores}\nos valores pares da lista são {pares}\nos valores impares da lista são {impares}')