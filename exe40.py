print('=-='*10)
print('Média escolar')
print('=-='*10)

nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))

media = (nota1+nota2)/2


print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,media))

if media >= 7:
    print('O aluno está APROVADO')
elif media >= 5 and media <= 6.9:
    print('0 aluno está em recuperação')
else:
    print('O aluno está REPROVADO')
