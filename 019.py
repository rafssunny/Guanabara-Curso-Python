from random import choice
aluno_1 = str(input('primeiro aluno:'))
aluno_2 = str(input('segundo aluno:'))
aluno_3 = str(input('terceiro aluno:'))
aluno_4 = str(input('aluno aluno:'))
sequencia = aluno_1, aluno_2, aluno_3, aluno_4
print(F'O aluno escolhido foi {choice(sequencia)}')