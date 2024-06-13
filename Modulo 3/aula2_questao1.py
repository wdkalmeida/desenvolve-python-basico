#Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17).
# Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos,
# indicando que podem entrar no bar, e False caso contrário.

#informação da idade
idade_Juliana = 17
idade_Cris = 18

#solicitar as idades de Juliana e Cris
idade_Cris = int(input("Digite a idade de Cris: "))
idade_Juliana = int(input("Digite a idade de Juliana: "))

#processamento
#True se os dois forem maior de idade
#Falso em qualquer outro caso
#<exp> 1: juliana é maior de idade
#<exp> 2: Cris é maior de idade
pode_entrar = idade_Juliana >= 18 and idade_Cris >= 18 

#Saida
print (pode_entrar)
