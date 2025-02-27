import random

Continuar = True
while Continuar:

    escolha_jogador = int(input('O que você escolherá?'))
    if (escolha_jogador == 1):
        print('Pedra')
    elif(escolha_jogador == 2):
        print('Papel')
    elif(escolha_jogador == 3):
        print('Tesoura')
    else:
        print('Você não escolheu algo selecionável.')

    escolha_computador = random.randint( 1, 3)
    if (escolha_computador == 1):
        print('Pedra')
    elif(escolha_computador == 2):
        print('Papel')
    elif(escolha_computador == 3):
        print('Tesoura')

    if (escolha_jogador == escolha_computador):
        print('Empate.')
    elif (escolha_jogador == 1 and escolha_computador == 2):
        print('Você perdeu.')
    elif (escolha_jogador == 2 and escolha_computador == 3):
        print('Você perdeu.')
    elif (escolha_jogador == 3 and escolha_computador == 1):
        print('Você perdeu.')
    elif (escolha_jogador == 1 and escolha_computador == 3):
        print('Você ganhou.')
    elif (escolha_jogador == 2 and escolha_computador == 1):
        print('Você ganhou.')
    elif (escolha_jogador == 3 and escolha_computador == 2):
        print('Você ganhou.')

    Continuar = (input('Deseja continuar?Y/N?').upper() == 'Y')

print('FIM DE JOGO.')