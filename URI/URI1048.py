A = float(input(''))
B = A + (A * 15 / 100)
C = A + (A * 12 / 100)
D = A + (A * 10 / 100)
E = A + (A * 7 / 100)
F = A + (A * 4 / 100)

if A <= 400.00:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %'.format(B, B - A))
elif A > 400 and A <= 800:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %'.format(C, C - A))
elif A > 800 and A <= 1200:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %'.format(D, D - A))
elif A > 1200 and A <= 2000:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %'.format(E, E - A))
else:
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %'.format(F, F - A))