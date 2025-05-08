from datetime import date
ano = int(input('Me diga algum ano e direi se é bissexto ou não, caso queira analisar o seu ano atual coloque 0: '))
ano_bissexto = ano%4
if ano == 0:
    ano = date.today().year
if ano_bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano de {ano} é bissexto')
else:
    print(f'o ano de {ano} não é bissexto')