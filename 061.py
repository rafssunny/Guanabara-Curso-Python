print('Progressão aritmética')
razao = int(input('Qual a razão dessa P.A?'))
termo = int(input('Qual o primeiro termo dessa P.A?'))
c = 0
while c != 10:
    print(termo, end = ' ➜ ')
    c+=1
    termo+=razao
print('FIM')
