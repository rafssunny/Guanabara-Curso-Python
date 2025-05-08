pessoas_p = dict()
pessoas = list()
media = 0
while True:
    pessoas_p['Nome'] = str(input('Nome:')).capitalize()
    pessoas_p['Sexo'] = ''
    while pessoas_p['Sexo'] not in ['M','F']:
        pessoas_p['Sexo'] = str(input('M/F: ')).upper()
        if pessoas_p['Sexo'] not in ['M','F']:
            print('Por favor digite somente M ou F')
    pessoas_p['Idade'] = int(input('Idade: '))
    media += pessoas_p['Idade']
    pessoas.append(pessoas_p.copy())
    pessoas_p.clear()
    pergunta = str(input('Quer continuar?sim/nao'))
    while pergunta not in ['nao', 'sim']:
        print('Responda apenas sim ou nao')
        pergunta = str(input('Quer continuar?sim/nao'))
    if pergunta == 'nao':
        break
media = media/len(pessoas)
print('-='*20)
print(f'-O grupo tem {len(pessoas)} pessoas.')
print(f'-A média de idade é {media:.2f} anos.')
print(f'-As mulheres cadastradas foram: ', end = '')
for pois, n in enumerate(pessoas):
    if pessoas[pois]["Sexo"] == 'F':
        print(f'{pessoas[pois]["Nome"]}', end = ' ')
print(f'\n-Lista das pessoas que estão acima da média: ')
for pos, p in enumerate(pessoas):
    if pessoas[pos]['Idade'] > media:
        print(f'-nome = {pessoas[pos]['Nome']}; sexo = {pessoas[pos]['Sexo']}; idade = {pessoas[pos]['Idade']}.')
print('')
print('<<<ENCERRADO>>>')