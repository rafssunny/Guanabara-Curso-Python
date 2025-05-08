valores = []
pergunta = ''
cont = 0
check = []
while True:
    valores.append(int(input('insira um valor:')))
    veredito = bool(valores[cont] in check)
    if veredito == True:
        print('valor não adicionado... pois já é existente')
        valores.pop()
        cont-=1
    if veredito == False:
        print('valor adicionado')
    pergunta = str(input('Deseja continuar? sim/nao')).lower()
    if pergunta == 'nao':
        valores.sort()
        print(f'Os valores digitados em ordem crescente são: {valores}')
        break
    check = valores[:]
    cont+=1