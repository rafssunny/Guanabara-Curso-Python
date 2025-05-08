print('Analisador')
media_idade = 0
maior = 0
nome_velho = ''
mulher = 0
for c in range(0,4):
    print('='*20)
    nome = str(input('NOME:')).capitalize()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO(M/F):')).upper()
    media_idade += idade
    if idade > maior:
        maior = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
print(20*'=')
print('ANALISADOR')
print('='*20)
print(f'A média de idade do grupo é {media_idade/4}')
print(f'O nome do homem mais velho é {nome_velho} e tem uma idade de {maior} anos')
print(f'{mulher} mulheres tem menos de 20 anos')