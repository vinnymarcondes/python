A, B = map(int, input().split())

if A % B == 0:
    print('Sao Multiplos')
elif B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')