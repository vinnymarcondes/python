Q = int(input("Digite a quantidade de elementos da PG: "))
P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
cont = 1

while cont <= Q:
 print("O", str(cont) + "º termo da PG é:", P)
 P = P * R
 cont = cont + 1

soma = (P // (R - 1))

print ("A soma dos termos da PG é:", soma)
