print('Check pra ver se é palíndromo')
palavra = str(input('Insira a palavra'))
palavra = palavra.strip('')
palavra = palavra.split()
palavra = ''.join(palavra)
letras = len(palavra)
for c in range(0, letras):
    verdade = (palavra[c::-1])
if palavra == verdade:
    print('É Políndromo ')
