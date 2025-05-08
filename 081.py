valores = []
cont = 0
pergunta = ''
while True:
    valores.append(int(input('Insira um número: ')))
    cont+=1
    pergunta = str(input('Quer continuar? sim/nao')).lower().strip()
    if pergunta == 'nao':
        break
valores.sort(reverse=True)
print(f'Foram digitados {cont} números, a lista de forma decrescente é {valores} e o valor 5 ', end = '')
if 5 in valores:
    print(f'está na lista', end = '')
else:
    print(f'não está na lista', end = '')