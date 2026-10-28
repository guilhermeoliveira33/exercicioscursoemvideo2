f = input('digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes'.format(f.count('A')))
print('a letra A aparece na posição {} '.format(f.find('A')+1))
print('A letra A aparece na ultima vez na posição {}'.format(f.rfind('A')+1))