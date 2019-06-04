a = float(input("Digite um valor para a: "))
b = float(input("Digite um valor para b: "))
c = float(input("Digite um valor para c: "))

d = b * b - 4 * a * c

if d < 0:
    print("A equação não possui raízes reais")
elif d == 0:
    x = (-1 * b + (d * 0.5)) / (2 * a)
    print("A raiz da equação é", x)
else:
    y = (-1 * b + (d * 0.5)) / (2 * a)
    z = (-1 * b - (d * 0.5)) / (2 * a)
    print("As raízes da equação são:", y, 'e', z)
