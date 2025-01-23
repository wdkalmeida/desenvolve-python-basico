#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
#Ex:Digite uma frase: O rato roeu a roupa do rei
#Frase modificada: * r*t* r*** * r**p* d* r**

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Define as vogais (maiúsculas e minúsculas)
vogais = "aeiouAEIOU"

# Substitui cada vogal por "*"
frase_modificada = "".join(["*" if char in vogais else char for char in frase])

# Exibe a frase modificada
print(f"Frase modificada: {frase_modificada}")
