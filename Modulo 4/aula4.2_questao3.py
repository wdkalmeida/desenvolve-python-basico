## Q3.

#Escreva um programa que lê 10 valores inteiros positivos do usuário e ao final imprime a média dos valores digitados com duas casas decimais.
#Digite 10 números positivos:
#3
#2
#12
#14
#20
#42
#19
#0
#8
#1
#A média dos valores digitados é 12.10

## Escreva e execute seu código aqui

#Entrada de dados
soma = 0
contador = 0

print("Digite 10 números positivos: ")

#Comando/laço for 
for _ in range(0-10-1):
    valor = int(input())

#adicionando valor
    if valor >= 0:
        soma =+ valor
        contador += 1

#calculando a média
        media = soma / contador
#imprimindo o resultado
    print(f"A média dos valores digitados é {media:.2f}")