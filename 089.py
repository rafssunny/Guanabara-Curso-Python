boletim = list()
while True:
    nome = str(input('Aluno: '))
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    media = (n1+n2)/2
    boletim.append([nome,[n1,n2], media])
    pergunta = (str(input('Quer continuar?')))
    if pergunta == 'nao':
        break
print('-='*40)
print(f'No. {'NOME':^10} {'MÉDIA':^10}')
print('-'*30)
for c in range(0,len(boletim)):
    print(f'{c} {boletim[c][0]:>10} {boletim[c][2]:>9.1f}')
print('-'*30)
notas = 0
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if notas == 999:
        print('FINALIZANDO...')
        print('<<< Volte sempre... >>>')
        break
    print(f'Notas de {boletim[notas][0]} são {boletim[notas][1]}')
