## Crie aqui a função soma_digitos() O desafio aqui é separar os dígitos de um número inteiro usando operações aritméticas
def soma_dígitos (n):
    soma = 0    
    while n > 0:    
        digito = n % 10 #extrair o dígito
        soma = soma + digito #soma os dígitos
        n = n // 10 #descartar o ultimo dígito do número
    return soma

#Solicitar ao usuário que insira um número inteiro
num = int(input("Digite um número inteiro: "))

#Calcular a soma dos dígitos
soma = soma_dígitos(num)    

#Exibir a soma dos dígitos  
print("A soma dos dígitos do número inserido é:", soma)