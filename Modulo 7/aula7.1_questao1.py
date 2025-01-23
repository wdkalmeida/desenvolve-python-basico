#Solicita o nome do usuario
nome = input("Digite seu nome: ")

#Itera sobre o tamanho do nome para criar a escada
#itera uma letra por vez e vai acrescentando na escada
for i in range(1,len(nome) + 1):
    print((nome[:i]))
          