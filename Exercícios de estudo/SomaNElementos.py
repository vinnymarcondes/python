A = int(input("Quantos números você quer somar? "))
cont = 1
soma = 0

while cont <= A:
    B = int(input("Digite o número a ser somado: "))
    if B >= 0:
        soma = soma + B
    cont = cont + 1
print("A soma dos números positivos é:", soma)
