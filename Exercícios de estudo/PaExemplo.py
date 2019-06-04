Q = int(input("Digite a quantidade de elementos da PA: "))
P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))

cont = 1

while cont <= Q:
 print("O", str(cont) + "º termo da PA é:", P)
 P = P + R
 cont = cont + 1
 soma = (Q * P) // 2 #fórmula errada

 
print ("A somatória dos termos da Pa é:", soma)
