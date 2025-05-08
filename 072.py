contagem = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze','doze','treze','quatorze', 'quinze', 'dezesseis', 'dezessete','dezoito', 'dezenove', 'vinte'
valor = int(input('Insira um valor entre 0 e 20 para ver por extenso.'))
while valor < 0 or valor > 20:
    valor = int(input('Tente novamente! Insira um valor entre 0 e 20:'))
print(contagem[valor])