PH = float(input("Digite o valor do PH: "))
if PH < 7.0:
    print("Solução ácida")
elif PH == 7.0:
    print("Solução neutra")
else:
    print("Solução básica")
