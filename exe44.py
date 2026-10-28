valor=float(input('Digite o valor do produto: R$'))
print('''Escolha uma forma de pagamento:
[1] Á vista no dinheiro ou cheque
[2] Á vista no cartão
[3] Em até 2x no cartão
[4] Em até 3x ou mais no cartão''')
opcao=int(input('Sua opção: '))
if opcao == 1:
    total = valor -(valor * 0.10)
elif opcao ==2:
    total = valor -(valor * 0.05)
elif opcao == 3:
  total = valor
  parcela = total / 2
  print('Sua comprar será parcelado em 2 x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 0.20)
    tortparcela = int(input('Quantas parcelas? '))
    parcela = total / tortparcela
    print('Sua comprar será parcelada em {}x de R${:.2f}'.format(tortparcela, parcela))
else:
    print('Opção invalida! Tente novamente.')

print('Sua comprar de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))



