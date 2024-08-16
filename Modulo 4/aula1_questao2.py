#iniciando o loop (while)
while True:
    n = int(input("Digite um valor para n: ")) #Lê o valor inteiro de n
    cont = 0 #valor inicial do contador

    if n < cont:
        while cont < n:
            cont += 1 #incrementa cont em 1
        print(cont)
        
    else:
        print("Fim")
