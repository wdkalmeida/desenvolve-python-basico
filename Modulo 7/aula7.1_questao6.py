#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos
#caracteres, mas caracteres rearranjados.
#Solicita a entrada da frase
frase = input("Digite uma frase: ")
#solicita a palavra objetivo
palavra_objetivo = input("Digite a palavra objetivo: ")
    #encontrando os anagramas da palavra objetivo
anagramas = []
for palavra in frase.split():
    if sorted(palavra) == sorted(palavra_objetivo):
        anagramas.append(palavra)

print(anagramas)