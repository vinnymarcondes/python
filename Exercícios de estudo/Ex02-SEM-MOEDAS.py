N = int(input(''))

cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0

print(N)
while N >= 100:
    N = N - 100
    cont100 = cont100 + 1
while N >= 50:
    N = N - 50
    cont50 = cont50 + 1
while N >= 20:
    N = N - 20
    cont20 = cont20 + 1
while N >= 10:
    N = N - 10
    cont10 = cont10 + 1
while N >= 5:
    N = N - 5
    cont5 = cont5 + 1
while N >= 2:
    N = N - 2
    cont2 = cont2 + 1

print('{} nota(s) de R$ 100,00'.format(cont100))
print('{} nota(s) de R$ 50,00'.format(cont50))
print('{} nota(s) de R$ 20,00'.format(cont20))
print('{} nota(s) de R$ 10,00'.format(cont10))
print('{} nota(s) de R$ 5,00'.format(cont5))
print('{} nota(s) de R$ 2,00'.format(cont2))
print('{} nota(s) de R$ 1,00'.format(N))