print('Cadastro')
sexo = pergunta = ''
idade = contagem = homens = mulheres = 0
while True:
    sexo = str(input('insira o sexo (M/F)')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('insira o sexo (M/F)')).upper().strip()
    idade = int(input('Insira a idade: '))
    if idade > 18:
        contagem+=1
    if sexo == 'M':
        homens+=1
    if idade < 20 and sexo == 'F':
        mulheres+=1
    pergunta = str(input('Deseja continuar?')).lower().strip()
    while pergunta != 'sim' and pergunta != 'nao':
        pergunta = str(input('Deseja continuar?')).lower().strip()
    if pergunta == 'sim':
        print('')
    else:
        break
print(f'{contagem} pessoas tem mais de 18 anos\n{homens} homens foram cadrastados\n{mulheres} mulheres tem menos de 20 anos')