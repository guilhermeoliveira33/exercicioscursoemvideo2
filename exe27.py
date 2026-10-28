nome = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')

# Divide o nome completo em uma lista de palavras
ni = nome.split()

print('Seu primeiro nome é {}'.format(ni[0]))
print('Seu último nome é {}'.format(ni[len(ni)-1]))

#  mostrar o nome na posicao len de nome -1 por que conta o zero
