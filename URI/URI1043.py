A,B,C = map(float, input().split())
area = ((A + B) * C) / 2
per = A + B + C

if A >= B + C:
    print('Area = {:.1f}'.format(area))
else:
    print('Perimetro = {:.1f}'.format(per))