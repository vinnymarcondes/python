a = [float(x) for x in input().split()]
a1 = sorted(a)

A = a1[2]
B = a1[1]
C = a1[0]


if A < 0 or B < 0 or C < 0:
    print()
elif A >= B + C:
    print('NAO FORMA TRIANGULO')
elif A ** 2 == B ** 2 + C ** 2:
    print('TRIANGULO RETANGULO')
elif A ** 2 > B ** 2 + C ** 2:
    print('TRIANGULO OBTUSANGULO')
    if A == B and B == C and A == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print('TRIANGULO ISOSCELES')

elif A ** 2 < B ** 2 + C ** 2:
    print('TRIANGULO ACUTANGULO')
    if A == B and B == C and A == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C:
        print('TRIANGULO ISOSCELES')



