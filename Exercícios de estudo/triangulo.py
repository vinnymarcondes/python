a = float(input("Digite o valor a: "))
b = float(input("Digite o valor b: "))
c = float(input("Digite o valor c: "))

if a >= b + c or b >= c + a or c >= a + b:
   print("Triângulo inexistente.")
elif a == b and b == c:
   print("Triângulo equilatero.")
elif a == b or b == c or c == a:
   print("Triângulo isósceles.")
else:
   print("Triângulo escaleno.")
