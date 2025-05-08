import requests
try:
    requests.get('https://pudim.com.br')
except:
    print('\033[1;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
