#Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade
# (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris,
# mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar,e False caso contrário.


#solicitar as idades de Juliana e Cris
idade_Cris = int(input("Digite a idade de Cris: "))
idade_Juliana = int(input("Digite a idade de Juliana: "))

#processamento
#True se pelo menos um dos dois forem maior de idade
#Falso em qualquer outro caso
#<exp> 1: juliana é maior de idade
#<exp> 2: Cris é maior de idade

pode_entrar = idade_Juliana >= 18 or idade_Cris >= 18 

#Saida
print (pode_entrar)