#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. 
# Dica: letra in "aeiou".

#Solucita a entrada da frase
frase = input("Digite uma frase: ")
#Verifica quantas vogais existem na frase
vogais = 0
#Verifica os indices das vogais e armazena em uma lista
indices_vogais = []
#Itera sobre o tamanho da frase - laço de repetição
for i in range(len(frase)):
    if frase[i] in "aeiou": #verifica se a letra da frase e uma vogal
        vogais += 1 #incrementa a quantidade de vogais no contador
        indices_vogais.append(i) #adiciona o indice da vogal na lista
        #exibe a quantidade de vogais e os indices das vogais
print(f"Quantidade de vogais: {vogais}")
print(f"Indices das vogais: {indices_vogais}")
