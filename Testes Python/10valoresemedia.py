#Entrada de dados
n = int(input("Quantidade de valores a serem lidos: "))

#variaveis iniciais
soma = 0
contador = 0
i = 0
#Comando/laço for 
for i in range(n): #pode ser usado (0,n,1)

    valor = int(input(f"Digite os valores positivos: "))

#adicionando valor
    if valor >= 0:
        soma =+ valor
        contador += 1

#calculando a média
        media = soma / contador
#imprimindo o resultado
    print(f"A média dos valores digitados é {media:.2f}")