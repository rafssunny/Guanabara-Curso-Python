frase = str(input('insira uma frase: '))
frase = frase.upper()
frase = frase.strip(' ')
print(f"""a letra A na frase aparece {frase.count('A')} vezes
A primeira posição que ele aparece é {frase.find('A')+1} 
A ultima posição que ele aparece é {frase.rfind('A')+1}""")