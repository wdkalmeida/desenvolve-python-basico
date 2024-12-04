#Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de 
#fatiamento de listas para criar uma lista domínios com o nome principal de todas as URLs, conforme exemplo a seguir.
#URLs: ["www.google.com&quot;, "www.gmail.com&quot;, "www.github.com&quot;, "www.reddit.com&quot;, "www.yahoo.com&quot;]
#dominios:  ["google", "gmail", "github", "reddit", "yahoo"]

# baixo um Opção menor de código
#urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
#dominios = [url[4:-4] for url in urls]
#print(dominios) 

# Lista original de URLs
URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista vazia para armazenar os nomes principais
dominios = []

# Laço que percorre cada URL na lista
for url in URLs:
    # Extrai o nome principal usando fatiamento
    nome_principal = url[4:-4]
    # Adiciona o nome principal à lista de domínios
    dominios.append(nome_principal)

# Exibe a lista de domínios
print(dominios)