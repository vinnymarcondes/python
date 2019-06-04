A = 1
S1 = 0
S2 = 0
while A != 0:
    A = int(input("Digite um número: "))
    if A < 0:
        S1 = A - S1
        print("A soma dos números negativos é:", S1)
    elif A > 0:
        S2 = A + S2
        print("A soma dos números positivos é:", S2)
