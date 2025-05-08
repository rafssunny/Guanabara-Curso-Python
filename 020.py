from random import shuffle
aluno_1 = str(input('Primeiro aluno: '))
aluno_2 = str(input('Segundo aluno: '))
aluno_3 = str(input('Terceiro aluno: '))
aluno_4 = str(input('Quarto aluno: '))
sequencia = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(sequencia)
print(f'A ordem de apresentação será:{sequencia}')