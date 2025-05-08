sexo = str(input('Qual seu sexo? (M/F)')).upper().strip()[0]
while sexo != 'M' and 'F':
    sexo = str(input('Por favor insira corretamente o sexo:')).upper().strip()[0]
if sexo == 'M':
    print('sexo masculino registrado com sucesso')
else:
    print('sexo feminino registrado com sucesso')