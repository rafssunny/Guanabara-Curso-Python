print('SUPER PROGRESSAO ARTIMETICA')
razao = int(input('Qual a razão dessa P.A? '))
termo = int(input('Qual o primeiro termo dessa P.A? '))
pergunta = ''
contagem = 0
termos = 0
quantidade = 0
while pergunta != 'nao':
    print(termo, end = '➜')
    contagem+=1
    termo+=razao
    if contagem == 10 or contagem == 10+termos:
        pergunta = str(input('\nQuer mostrar mais termos? sim/nao')).lower()
        if pergunta == 'sim':
            termos += int(input('Quantos termos a mais?'))
    if pergunta == 'nao':
        print('blz finalizado.')
    quantidade = 10+termos
print(f'Progressão finalizada com {quantidade} termos mostrados')

