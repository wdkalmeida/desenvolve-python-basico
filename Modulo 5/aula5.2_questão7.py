#Escreva um programa que pergunte ao usuário qual operação ele deseja: maior ou menor.
#Em seguida leia uma quantidade indefinida de valores do usuário, até que o usuário digite o valor zero.
#Apresente ao final o maior ou menor dos valores digitados de acordo com a escolha do usuário.

#**Sua solução deve incluir pelo menos uma função ```lambda```** para resolver o problema.
#Exemplo de interação:
#Opções: (1) maior ou (2) menor?
#Opção: 1
#Digite os valores de entrada. Digite 0 para finalizar a entrada de valores.
#4
#12
#15
#1
#0
#O maior valor é: 15

#Crie aqui sua função lambda
encontrar_maior = lambda x, y: x if x > y else y
encontrar_menor = lambda x, y: x if x < y else y

#Solicite ao usuário qual operação ele deseja: maior ou menor
opcao = int(input("Opções: (1) maior ou (2) menor? "))  
#Leia uma quantidade indefinida de valores do usuário, até que o usuário digite o valor zero
valores = []
while True:     
    valor = int(input("Digite os valores de entrada. Digite 0 para finalizar a entrada de valores. "))
    if valor == 0:
        break
    valores.append(valor)
#Apresente ao final o maior ou menor dos valores digitados de acordo com a escolha do usuário
print("O maior valor é:", max(valores) if opcao == 1 else min(valores))