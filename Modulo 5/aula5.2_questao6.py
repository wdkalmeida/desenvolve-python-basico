#Crie uma função lambda para verificar se um número é par ou ímpar. Em seguida, solicite ao usuário um número indefinidos de valores (até que o usuário digite 0). Para cada valor de entrada, informe se é par ou ímpar.

#Exemplo de interação:
#Digite os valores que deseja verificar a paridade (digite 0 para finalizar a entrada de dados):
#3
#ímpar
#8
#par
#12
#par
#5
#ímpar
#7ímpar

#Função para verificar se um número é par ou ímpar
par_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

#Solicita ao usuário um número indefinidos de valores (até que o usuário digite 0)
while True:
    num = int(input("Digite um número (0 para encerrar): "))
    if num == 0:
        break   
    print(par_impar(num))   
    