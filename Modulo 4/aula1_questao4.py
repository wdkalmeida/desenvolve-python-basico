#inicio das variáveis
while True:

#Lê o valor de n
    n = int(input("Digite a quantidade de números que serão lidos: "))

# valor inicial de maior = 0
    Maior = 0

#Verifica se n > 0
    while n > 0:

        #lê o valor de x 
        x = int(input("Digite um valor: "))

        #verifica se x é maior que maior
        if x > Maior:
            
        #Se sim, atualiza maior para ser igual a x
            Maior = x

        #Diminui o valor de n em 1 (n = n-1)
        n -= 1

         #termino do loop
        print("O maior valor digitado foi:", Maior) 

