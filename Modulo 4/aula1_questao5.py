#Exercício 5
#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes.
#Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente.
#Ao final, imprima a média das idades.
#(idade1 + idade2 + idade3 + … + idade_n)/N

qtdRespondentes = input("Quantos respondentes? ")
idadeTotal = 0
i = 1

#for i in range(int(qtdRespondentes)): (Outra opção)
while i <= int(qtdRespondentes):
    idade = input("Idade: ")
    idadeTotal = idadeTotal + int(idade)
    i = i + 1

media = idadeTotal / int(qtdRespondentes)
print(f"A média das idades é {media:.0f} anos")
#print(f"Media das idades: {media:.2f}")(outra opção)