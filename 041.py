from datetime import date
Ano = int(input('Qual seu ano de nascimento? '))
Ano_atual = date.today().year
idade = Ano_atual-Ano
print(f'Sua idade é de {idade} anos')
if idade <= 9:
    print('Você é Mirim')
elif idade > 9 and idade <= 14:
    print('Você é Infantil')
elif idade > 14 and idade <= 19:
    print('Você é Junior')
elif idade > 19 and idade == 20:
    print('Você é Sênior')
else:
    print('Você é Master')