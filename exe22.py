nome = str(input('Digite seu nome completo: ')).strip()



print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


# len(frases) mostrar os caracteres
# frase.count('o') conta quantas vez tem a letra no parentesesees marcado como string
# frase.find('deo) procura a parte que tem no parentessse
# curso in frase true or false
# frase.replace('python,'Android) trasformação trocar caracters
# frase.upper() mostra todas as letra em maiusculo
# frase.lower() mostra todas as letras em minusculo
# frase.capitalize() vai jogar todos os caracteres para minusculo e so o primeiro caracter vai ficar em maiusculo
# frase.title() ele vai fazer uma análise mais profundo do que o capitalize analizando quantas palavras tem onde tiver espaço ele vai fazer uma quebra dde palavra e vai fazer capitalize palavra por palavra
# frase.strip() ele vai tirar todos os espaços "inúteis"
# frase.rstrip() remove espaços do lado direito
# frase.lstrip() remove espaços do lado esquerdo
# frase.split()  vai ocorrer uma divisão entre as Strings considerando os espaços onde ocorrer espaço vai acontecer uma divisão vai dividir em pedacos e recomeça a numeração nas divisões, cada palavra recebe uma indetização nova, ele gera uma lista com todas as palavras de uma cadeia de caracteres
# junção '-'join(frase) se voce tem tem nome separados podemos os usar o join para juntar e usar o caracter nas aspas

# exemplos

# frase = 'curso em video python '
#  frase = frase.replace('python', 'android')
#  print('curso in frase)

# print(frase.lower().find('video'))

# outro exemplo

# frase = ('curso em vídeo')
# print(frase.split()) criar uma lista

# frase = ('curso em vídeo')
# dividido = frase.split()
# print(dividido[0][2]) para mostrar a parte e letra
