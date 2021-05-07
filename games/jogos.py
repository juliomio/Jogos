import adivinhacao01
import forca

def escolhe_jogo():
    print('-'*17)
    print('Escolha seu Jogo')
    print('-'*17)

    print('Jogo Adivinhação (1)  Jogo Forca (2) ')
    jogo = int(input(' Defina seu jogo: '))

    if jogo == 1:
        print('Jogando Adivinhação')
        adivinhacao01.jogar_ad()
    else:
        print('Jogando Forca')
        forca.jogar_f()

if (__name__ == '__main__'):
    escolhe_jogo()