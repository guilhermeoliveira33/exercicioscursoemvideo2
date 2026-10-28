n1 = int(input('Digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))

# verificando menor
menor = n1
if n2 <n1 and n2 <n3:
    menor = n2
if n3 <n2 and n3 <n1:
    menor = n3
# verificando maior
maior = n1
if n1 <n2 and n3 <n2:
    maior = n2
if n2 <n3 and n1 <n3:
    maior = n3

print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))



