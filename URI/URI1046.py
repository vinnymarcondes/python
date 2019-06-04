A, B = input().split(' ')

A = int(A)
B = int(B)

if A == B:
    print('O JOGO DUROU {} HORA(S)'.format(24))
elif A < B:
    print('O JOGO DUROU {} HORA(S)'.format(B - A))
else:
    print('O JOGO DUROU {} HORA(S)'.format(24 - A + B))