from random import randint
computador = randint(0, 5) #faz o computador sortear um número
print('-+-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-+-' * 20)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))