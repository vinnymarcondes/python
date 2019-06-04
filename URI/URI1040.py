N1, N2, N3, N4 = input().split(' ')
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
NE = 0

Med = ((N1 * 2) + (N2 * 3) + (N3 * 4) + N4) / 10

if Med >= 7:
    print('Media: {:.1f}'.format(Med))
    print('Aluno aprovado.')
    quit()
elif Med < 5:
    print('Media: {:.1f}'.format(Med))
    print('Aluno reprovado.')
    quit()
elif Med >= 5.0 and Med <= 6.9:
    print('Media: {:.1f}'.format(Med))
    print('Aluno em exame.')
    NE = float(input(''))
    print('Nota do exame: {:.1f}'.format(NE))
    NE = (Med + NE) / 2
if NE >= 5.0:
    print('Aluno aprovado.')
    print('Media final: {:.1f}'.format(NE))
else:
    print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(NE))

