#iniciando o loop
while True:
    n1 = int(input("Digite um valor para n1: ")) #Lê o valor inteiro de n1

    n2 = int(input("Digite um valor para n2: ")) #Lê o valor inteiro de n2

    n3 = int(input("Digite um valor para n3: ")) #Lê o valor inteiro de n3

    m = (n1 + n2 + n3) / 3

    if m >= 60:
        print("Aprovado")
        print("Fim")

    elif m >= 40:
        print("Recuperação")
        print("Fim")

    else:
        print("Reprovado")
        print("Fim")
        


