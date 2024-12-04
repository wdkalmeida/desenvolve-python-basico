### Q2.
#Dado um número inteiro positivo informado pelo usuário, crie um programa em Python que utilize o comando for para calcular e exibir a soma dos números
#de 1 até o número informado. Ou seja, $1 + 2 + 3 + ... + n$
#Exemplo de interação:
#Digite um número: 5
#A soma dos números de 1 a 5 é 15

## Escreva e execute seu código aqui

#Entrada de dados
n = int(input("Digite um número: "))

#inicializa a variavel soma
soma = 0

#Comando/laço for para somar os números de 1 até N 
for i in range(1, n + 1):
    soma += i

#imprimindo o resultado
    print(f"Soma dos números de 1 a {n} é {soma}")