#*************************************************************#
#          Faculdade de Tecnologia - FATEC São Paulo          #
# Análise e Desenvolvimento de Sistemas - Noite - 1º Sem 2019 #
# Algoritmos e Lógica de Programação - Prof Sérgio Luiz Banin #
#                                                             #
#        Projeto Programa 2 - Totalização Simples de          #
#                             de vendas de produtos           #
#                                                             #
# GRUPO 5:                                                    #
# LUCAS FERNANDES PIRES DA SILVA                 RA: 19100646 #
# LUCIANE CRISTINA NAGAY MARTINS            	 RA: 19100682 #
# VANESSA REGINA DE JESUS DA SILVA          	 RA: 19100397 #
# VINICIUS DE PAULA MARCONDES	                 RA: 19110938 #
#*************************************************************#

Arquivo = open('vendas.txt')
Lista = []
Total = 0

for Linha in Arquivo:
    Item = Linha.split(';')

    Item[0] = int(Item[0])
    Item[1] = int(Item[1])
    Item[2] = float(Item[2])

    Lista.append(Item)

Arquivo.close()

for Venda in Lista:
    Total += Venda[2] * Venda[1]

CodProd = int(input('Digite o código: '))

while CodProd != 0:
    TotProd = 0
    Valido = ''

    for Venda in Lista:

        if CodProd in Venda and CodProd > 10000 and CodProd < 21000:

            TotProd += Venda[2] * Venda[1]
            Valido = True

    if Valido:
        print('Total vendido do produto {0} = R$ {1:.2f}'.format(CodProd, TotProd))
    else:
        print('Código inválido')
        print('-'*30)
    CodProd = int(input('Digite o código: '))
