#Escreva uma função em Python chamada ```soma_quadrados``` que recebe dois números como parâmetros e retorna a soma dos seus quadrados. 
#No programa principal solicite ao usuário que insira dois números e utilize a função para exibir a soma dos quadrados.

## Crie aqui a função soma_quadrados()
def soma_quadrados(n1, n2):
    resultado = n1 ** 2 + n2 ** 2
    return resultado

#Solicitar ao usuário que insira dois números
num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: "))  

#Calcular a soma dos quadrados
soma = soma_quadrados(num1, num2)

#Exibir a soma dos quadrados
print("A soma dos quadrados dos números inseridos é:", soma)