import random


def jogar_ad():

    print('-'*32)
    print('Bem Vindo ao Jogo da Advinhação')
    print('-'*32)


    numero_secreto = random.randrange(1, 101)
    rept = 0
    chances = 1
    pontos = 1000

    print('Nível de dificuldade: (1)Facil (2) Medio (3) Dificil')
    nivel = int(input('Defina o nivel de dificuldade: '))
    print(f'Você escolher o nivel {nivel}')

    if nivel == 1:
        rept = 20
    elif nivel == 2:
        rept = 10
    else:
        rept = 5

    for chances in range(1, rept+1):
        print(f'Tentativa {chances} de {rept}')
        num = int(input('Digite um número: '))

        if num > 100 or num < 1:
            print('Você deve escrever um numero entre 1 e 100, por gentileza ...')
            continue

        maior = num < numero_secreto
        menor = num > numero_secreto

        if maior:
            print('O numero secreto é maior')
            if chances == rept:
                print('Infelizmente suas chances acabaram .. tente novamente mais tarde')
        elif menor:
            print('O numero secreto é menor ')
            if chances == rept:
                print('Infelizmente suas chances acabaram .. Tente novamente mais tarde')
        else:
            print('Parabens .. Você acertou !!')
            print(f'Você fez {pontos} pontos')
            break
        pontos_perdidos = abs(numero_secreto - num)
        pontos = pontos - pontos_perdidos

if __name__ == '__main__':
    jogar_ad()


    print('Fim de jogo .. ')
