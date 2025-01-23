#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo
#(ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, 
#e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

while True:
    frase = input("Digite uma frase: ")
    #verifica se o usuario digitou "Fim"
    if frase.strip().lower() == "fim":
        break
    #Normaliza a frase removendo espaços e pontuação
    frase = frase.lower().replace(" ", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    #verifica se a frase digitada é um palíndromo
    if frase == frase[::-1]:
        print("A frase digitada é um palíndromo.")
    else:
        print("A frase digitada não é um palíndromo.")
    #Programa Encerrado
print("Programa encerrado.")