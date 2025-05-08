numero = 0
contagem = 0
maior = 0
menor = 0
soma = 0
pergunta = ''
while pergunta != 'nao':
    numero = float(input('Insira um valor: '))
    if contagem == 0:
        maior+=numero
        menor+=numero
    if numero > maior:
        maior-=maior
        maior+=numero
    if numero < menor:
        menor-=menor
        menor+=numero
    soma+=numero
    contagem += 1
    pergunta = str(input('quer continuar?(sim/nao): '))
print(f'A média entre os valores é de {soma/contagem:.2f}, o maior valor inserido foi {maior:.0f} e o menor foi {menor:.0f}  ')
