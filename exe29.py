velocidade = int(input('qual é a velocidade atual do carro: '))
if velocidade <=80:
    print('Multado! Você excedeu o limite permitido!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia!')



