#Você está desenvolvendo um programa para auxiliar em cálculos de geometria básica. Crie as seguintes funções: 
# A função 
#calcula_perimetro_triangulo()
#que recebe três inteiros correspondentes aos lados de um triângulo e retorna o perímetro do triângulo, ou seja, a soma dos seus lados.
# A função 
#calcula_perimetro_circulo()
#que recebe um inteiro referente ao raio do círculo e retorna o perímetro do círculo, dado por $2 \pi r$. Use a constante $\pi$ da biblioteca 
#math
#A função 
#calcula_perimetro_retangulo()
#que possui um parâmetro obrigatório 
#lado1 e um opcional 
#lado2, ambos inteiros. Se o valor opcional não for fornecido, significa que se trata de um quadrado. Sua função deve calcular e 
#retornar o perímetro do retângulo, ou seja, a soma de seus lados. 
 #- Para o quadrado, é dado por $4 \times lado1$
 #- Para o retângulo é dado por $2 \times lado1 + 2 \times lado2$
    
#No programa principal apresente um menu com as opções disponíveis do seu sistema e uma quarta opção 
#Sair
#. Solicite ao usuário a opção desejada, solicite as entradas correspondentes à opção escolhida, invoque a respective função e apresente
# o seu retorno. Seu programa deve retornar ao menu até que o usuário escolha a opção 
#Sair

#Crie aqui a função calcula_perimetro_triangulo()
import math

def calcula_perimetro_triangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro    

#Crie aqui a função calcula_perimetro_circulo() 
def calcula_perimetro_circulo(raio):
    perimetro = 2 * math.pi * raio
    return perimetro        

#Crie aqui a função calcula_perimetro_retangulo()
def calcula_perimetro_retangulo(lado1, lado2 = 0):
    if lado2 == 0:
        perimetro = 4 * lado1
    else:
        perimetro = 2 * lado1 + 2 * lado2
    return perimetro        

#Crie aqui o programa principal 
while True:
    print("Selecione uma opção:")
    print("1 - Triângulo")
    print("2 - Círculo")
    print("3 - Retângulo")
    print("4 - Sair")
    opcao = int(input())
    if opcao == 1:
        lado1 = int(input("Lado 1: "))
        lado2 = int(input("Lado 2: "))
        lado3 = int(input("Lado 3: "))
        perimetro = calcula_perimetro_triangulo(lado1, lado2, lado3)
        print("Perimetro é:", perimetro)
    elif opcao == 2:
        raio = int(input("Raio: "))
        perimetro = calcula_perimetro_circulo(raio)
        print("Perimetro:", perimetro)
    elif opcao == 3:
        print("Informe os dois lados do retângulo. Se for um quadrado, digite 0 para o segundo valor:")
        lado1 = int(input("Lado 1: "))
        lado2 = int(input("Lado 2: "))        
        perimetro = calcula_perimetro_retangulo(lado1, lado2)
        print("O Perimetro é:", perimetro)
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")    
        