#Exerciciom 6.5 - 1 
#Lista de listas representando os lados de multiplos triangulos
triangulos = [[2,2,2], [3,4,5], [3,2,2],[4,4,4]]

#Função para verificar se um triângulo é equilatero
def testa_equilatero(lados):
    return lados[0] == lados[1] == lados[2]
    
#Usando filter para filtrar os triângulos equilateros
triangulos_equilateros = filter(testa_equilatero, triangulos)

#Imprimindo os triângulos equilateros e originais
print("Triângulos originais: ",list(triangulos))
print("Triângulos equilateros: ",list(triangulos_equilateros))