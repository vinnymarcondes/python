#*************************************************************#
#          Faculdade de Tecnologia - FATEC São Paulo          #
# Análise e Desenvolvimento de Sistemas - Noite - 1º Sem 2019 #
# Algoritmos e Lógica de Programação - Prof Sérgio Luiz Banin #
#                                                             #
#        Projeto Programa 1 – Cálculo de Médias               #
#               Tentativa 07                                  #
#                                                             #
# GRUPO 5:                                                    #
# LUCAS FERNANDES PIRES DA SILVA                 RA: 19100646 #
# LUCIANE CRISTINA NAGAY MARTINS            	 RA: 19100682 #
# VANESSA REGINA DE JESUS DA SILVA          	 RA: 19100397 #
# VINICIUS DE PAULA MARCONDES	                 RA: 19110938 #
#*************************************************************#
arquivo = open('ALUNOS.TXT', 'r')
linha = arquivo.readline()
linha = linha.rstrip()
M = 'Matrícula'
N = 'Nome'
F = "Final"
R = 'Situação'
print('{}{:>10}{:>63}{:>12}'.format(M, N, F, R))
while linha != '':
    linha = str.split((linha), ";")
    p1 = float(linha[2])
    p2 = float(linha[3])
    nt = float(linha[3])
    media = ((4*p1)+(4*p2)+(2*nt))/10
    if media >= 6:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    print("{:<15}{:<40}{:>25.1f}{:>14}".format(
        linha[0], linha[1], media, resultado))
    linha = arquivo.readline()
    linha = linha.rstrip()
arquivo.close()
print("\nFim do Programa")
