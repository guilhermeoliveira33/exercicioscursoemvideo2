print("-=-"*10)
print('Emprestimo bancário ')
print('-=-'*10)

valor=float(input('Qual o valor da casa: R$'))
salario=float(input('Qual o seu salário: R$'))
tempo=int(input('Quantos anos de financiameto: '))

prestacao=valor/ (tempo*12)
excedente = salario*30/100


print('Para pagar uma casa de {:.2f} em {} anos'.format(valor,tempo), end= "")
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao<excedente:
    print('Seu financiamento foi aprovado!')
else:
    print('Seu financiamento foi reprovado!')





