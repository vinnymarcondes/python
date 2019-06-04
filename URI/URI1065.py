A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
cont = 0

if A % 2 == 0:
    cont = cont + 1
if B % 2 == 0:
    cont = cont + 1
if C % 2 == 0:
    cont = cont + 1
if D % 2 == 0:
    cont = cont + 1
if E % 2 == 0:
    cont = cont + 1

print('{} valores pares'.format(cont))