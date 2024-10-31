#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação 
# apresentada a seguir:
#Data: 15/03/2023 
#Hora: 14:05
#Você pode consultar esse tutorial da Alura sobre a biblioteca datetime. Existem várias maneiras de resolver essa questão.
# Uma sugestão é:
#Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute
#Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 2 dígitos 
# precedidos por zero se necessário.

import datetime

#Exibe a data e hora atuais
print(f"Data: {datetime.datetime.now().day:02d}/{datetime.datetime.now().month:02d}/{datetime.datetime.now().year:02d}")
print(f"Hora: {datetime.datetime.now().hour:02d}:{datetime.datetime.now().minute:02d}") 