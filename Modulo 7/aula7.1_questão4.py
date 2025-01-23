#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente.
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

celular = input("Digite o numero de celular: ")
#verifica se o número tem 8 dígitos
if len(celular) == 8:
    #adiciona o 9 na frente
    celular = "9" + celular
    print("Número corrigido: ", celular[:5] + "-" + celular[5:])
elif len(celular) == 9 and celular[0] == "9":
    #número já correto
    print("Número válido: ", celular[:5] + "-" + celular[5:])
else:
    celular = celular