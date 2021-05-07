import random

def cabecalho():
    print('-' * 27)
    print('Bem Vindo ao Jogo da Forca')
    print('-' * 27)

def carrega_palavras():
    arquivo = open("palavras.txt", "r")

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    lista = ['_' for letra in palavra]
    return lista

def pede_chute():
    print()
    chute = (input('Fale sua letra ? '))
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def jogar_f():
    cabecalho()
    palavra_secreta =carrega_palavras()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        if erros == 6:
            break
        if ('_' not in letras_acertadas):
            break

        print(letras_acertadas)

    if ('_' not in letras_acertadas):
        print(letras_acertadas)
        print('Voce acertou !!')
    else:
        print('Voce errou !!')

    print('Fim de Jogo...')


if (__name__ == '__main__'):
    jogar_f()
