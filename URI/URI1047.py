A, B, C, D = input().split(' ')

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if A == C and B == D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24, 0))
elif A < C and B == D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(C - A, 0))
elif A > C and B == D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 - A + C, 0))
elif A == C and B < D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(0, D - B))
elif A < C and B < D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(C - A, D - B))
elif A > C and B < D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 - A + C, D - B))
elif A == C and B > D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 -1, 60 - B + D))
elif A < C and B > D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(C - A - 1, 60 - B + D))
elif A > C and B > D:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(23 - A + C, 60 - B + D))