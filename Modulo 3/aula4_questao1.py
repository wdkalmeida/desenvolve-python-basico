#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do
# número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

n1, n2 = int(input("Digite um número: ")), int(input("Digite um número: "))
if ((n1 + n2)% 2) == 0: 
    print("É par")
else:
    print("É impar")

    # Outra forma de fazer essa expressão de maneira mais curta é usando operador ternario:
    # ex: n1,n2 = int(input()), int(input())
    #     print("É par" if (n1+n2) % 2 == 0 else "É impar")
