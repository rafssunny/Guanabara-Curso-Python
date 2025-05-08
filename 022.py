erika = str(input('me diga o seu nome completo:'))
print(f'seu nome em maiusculo é {erika.upper()}')
print(f'seu nome em minusculo é {erika.lower()}')
littlekitty = erika.split()
erika_linda = ''.join(littlekitty)
erika_meuamor = erika_linda.strip('')
print(f'Seu nome completo tem {len(erika_meuamor)} letras')
erika_meubem = '+'.join(littlekitty)
erika_meuamor = erika_meubem.find('+')
print(f'seu primeiro nome tem {erika_meuamor} letras')


