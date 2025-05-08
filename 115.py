import Cadastro
from Cadastro import arquivo

Lista_original = list()
arq = 'cadastrosistema.txt'
if not arquivo.ArquivoExiste(arq):
    arquivo.CriarArquivo(arq)
opcao = 0
end = False
while True:
    Cadastro.Menu()
    while True:
        try:
            opcao = int(input('\033[0;33mSua Opção: \033[m'))
            if opcao in [1, 2, 3]:
                print('-' * 50)
                break
            else:
                print('\033[1;31mERRO: Insira uma opção válida!\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mPROGRAMA ENCERRADO PELO USUÁRIO.\033[m')
            end = True
            break
        except:
            print('\033[1;31mERRO: Insira uma opção válida!\033[m')
    if opcao == 1:
        Cadastro.Sistema(Lista_original, arq)
    elif opcao == 2:
        Cadastro.Cadastro(Lista_original, arq)
    elif opcao == 3:
        print('\033[3;34mENCERRADO. VOLTE SEMPRE.\033[m')
        break
    if end:
        break
