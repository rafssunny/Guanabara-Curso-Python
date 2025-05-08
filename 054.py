from datetime import date
print('Já atingiu a maioridade? ')
soma_1 = 0
soma_2 = 0
for c in range(0, 7):
    ano = int(input('Insira o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        soma_1+=1
    else:
        soma_2+=1
    idade -= idade
print(f'{soma_1} Pessoas já atingiram a maioridade e {soma_2} ainda não atingiram')