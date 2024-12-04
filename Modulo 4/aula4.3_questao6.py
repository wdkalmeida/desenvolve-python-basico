### Q6.

#Escreva um programa que lê uma quantidade indefinida de valores e informa o maior e o menor valor digitados.
#A leitura é encerrada quando o usuário digitar o valor 0 (zero).
#Entrada:
#12
#-1
#29
#11
#-5
#0
#Saída:
#Maior: 29
#Menor: -5

### Escreva e execute seu código aqui
#Estado inicial das variáveis
maior = float('-inf')
menor = float('inf')

while True: 
    n = int(input())
    if n == 0: break

    #Atualiza o valor de Maior
    if n > maior:
        maior = n
    #Atualiza o valor de Menor
    if n < menor:
        menor = n  
    #imprime os valores de maior e menor após cada entrada
        print(f"O maior valor é:{maior}")
        print(f"O menor valor é:{menor}")