from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções são as seguintes:
\033[1;34m[ 0 ] Pedra \033[m
\033[1;34m[ 1 ] Papel \033[m
\033[1;34m[ 2 ] Tesoura\033[m''')
jogador = int(input('Qual sua jogada ?   '))
print('\033[1;33mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;33mPO\033[m')
print('-='*16)
print('O computador escolheu \033[1;34m{}\033[m'.format(itens[pc]))
print('O jogador escolheu \033[1;34m{}\033[m'.format(itens[jogador]))
print('-='*16)

if pc == 0: # pedra
    if jogador == 0:
        print('\033[1;32mQUE PENA\033[m .. O jogo deu \033[1;32mEMPATE\033[m')
    elif jogador == 1:
        print('O \033[1;34mJOGADOR VENCEU\033[m essa partida')
    elif jogador == 2:
        print('O \033[1;33mCOMPUTADOR VENCEU\033[m essa partida')
    else:
        print('PARTIDA INVÁLIDA')
if pc == 1:
    if jogador == 0:
        print('O  \033[1;33mCOMPUTADOR VENCEU\033[m essa partida')
    elif jogador == 1:
        print('\033[1;32mQUE PENA\033[m .. O jogo deu \033[1;32mEMPATE\033[m')
    elif jogador == 2:
        print('O \033[1;34mJOGADOR VENCEU\033[m essa partida')
    else:
        print('PARTIDA INVÁLIDA')
if pc == 2:
    if jogador == 0:
        print('O \033[1;34mJOGADOR VENCEU\033[m essa partida')
    elif jogador == 1:
        print('O  \033[1;33mCOMPUTADOR VENCEU\033[m essa partida')
    elif jogador == 2:
        print('\033[1;32mQUE PENA\033[m.. O jogo deu \033[1;32mEMPATE\033[m')
    else:
        print('PARTIDA INVÁLIDA .. Tente Novamente')

