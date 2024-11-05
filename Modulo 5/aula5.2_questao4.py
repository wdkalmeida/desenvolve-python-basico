#Crie a função ```inverteValor()``` que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando apenas 
# operações aritméticas
# Crie a função ```verificaInverso()``` que recebe o valor original e o valor invertido e retorna verdadeiro se ambos forem 
# igualmente par ou igualmente ímpar. Retorne falso caso contrário.
# No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.

#Crie a função ```inverteValor()``` que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando apenas
# operações aritméticas
def inverteValor(n):    
    invertido = 0
    while n > 0:
        ultimo_digito = n % 10
        invertido = invertido *10 + ultimo_digito
        n = n // 10
    return invertido

#Crie a função ```verificaInverso() que recebe o valor original e o valor invertido e retorna verdadeiro se ambos forem
# igualmente par ou igualmente ímpar. Retorne falso caso contrário.
def verificaInverso(valor_original, valor_invertido):
    return valor_original % 2 == valor_invertido % 2

#No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.
original = int(input("Digite um número inteiro: "))
invertido = inverteValor(original)
verificado = verificaInverso(original, invertido)
print(f"O inverso de {original} é {invertido} e são igualmente par ou impar? {verificado}")