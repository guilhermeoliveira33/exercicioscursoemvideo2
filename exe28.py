import random
from time import sleep

print("-=-" * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
n = int(input('em que número pensei: '))


print('PROCESSANDO...')
sleep(3)

# O randint(0, 5) escolhe direto um número de 0 até 5 (incluindo o 5)
escolhido = random.randint(0, 5)

if n == escolhido:
    print('PARABÉNS você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(escolhido, n))
