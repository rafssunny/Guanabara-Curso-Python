escola = {'Aluno':str(input('Aluno: ')), 'Média':float(input('Média: '))}
print(f'Nome é igual a {escola['Aluno']}\nMédia é igual a {escola['Média']}')
if escola['Média'] >= 7:
    escola['Situação'] = 'Aprovado'
elif escola['Média'] < 7 and escola['Média'] >= 5:
    escola['Situação'] = 'Recuperação'
else:
    escola['Situação'] = 'Reprovado'
print(f'Situação é igual a {escola['Situação']}')