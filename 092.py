import datetime
trabalho = dict()
trabalho['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
trabalho['Idade'] = datetime.datetime.today().year-nascimento
trabalho['CTPS'] = int(input('Carteira de Trabalho: '))
if trabalho['CTPS'] > 0:
    trabalho['Ano'] = int(input('Qual o ano de contratação?'))
    trabalho['Salario'] = float(input('Qual o salário?R$ '))
    trabalho['Aposentadoria'] = trabalho['Idade']+(35-(datetime.datetime.today().year-trabalho['Ano']))
print('-='*30)
for c, n in trabalho.items():
    print(f'{c} tem o valor {n}')


