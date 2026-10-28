from random import randint
from time import sleep

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogada = int(input('Sua jogada: '))

# Validação simples para evitar que o jogador digite um número inválido
if jogada < 0 or jogada > 2:
    print('Jogada inválida!')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)

    # Corrigido para sortear entre 0 e 2, igual às opções do jogador
    computador = randint(0, 2)
    itens = ('Pedra', 'Papel', 'Tesoura')

    print('-=-' * 10)
    # Corrigido a ordem dos prints para exibir o que cada um realmente jogou
    print('Computador jogou: {}'.format(itens[computador]))
    print('Jogador jogou: {}'.format(itens[jogada]))
    print('-=-' * 10)

    # Lógica do jogo corrigida usando 0 (Pedra), 1 (Papel) e 2 (Tesoura)
    if jogada == computador:
        print('EMPATE!')
    elif (jogada == 0 and computador == 2) or \
         (jogada == 1 and computador == 0) or \
         (jogada == 2 and computador == 1):
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
