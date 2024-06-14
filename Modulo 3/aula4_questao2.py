#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários.
#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.
#O programa deve imprimir uma mensagem correspondente à classificação do filme:

#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

#Entrada de dados
filme = input("Digite o nome do filme: " )
avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))

#verificação da avaliação e impressão da mensagem 
if avaliacao == 5:
    print("excelente")
elif avaliacao == 4:
    print("Muito Bom")
elif avaliacao == 3:
    print("Bom")
elif avaliacao == 2:
    print("Regular")
elif avaliacao == 1:
    print("Ruim")
else:
    print("Avaliação invalida. Insira uma valor de 1 a 5.")