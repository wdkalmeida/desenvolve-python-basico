import csv

# Lista para armazenar as músicas processadas
musicas = []

# Abrindo o arquivo CSV
with open("spotify-2023.csv", encoding="latin-1") as file:
    reader = csv.reader(file)
    next(reader)  # Pulamos o cabeçalho

    for row in reader:
        try:
            track_name = row[0]  # Nome da música
            artist_name = row[1]  # Nome do artista
            released_year = int(row[3])  # Ano de lançamento
            streams = int(row[8])  # Número de streams

            # Filtro para músicas lançadas entre 2012 e 2022
            if 2012 <= released_year <= 2022:
                musicas.append([track_name, artist_name, released_year, streams])

        except ValueError:
            continue  # Ignorar linhas inválidas

# Selecionar a música mais tocada de cada ano
top_musicas = {}

for musica in musicas:
    track_name, artist_name, released_year, streams = musica

    # Se o ano ainda não estiver no dicionário ou se encontramos uma música com mais streams, atualizamos
    if released_year not in top_musicas or streams > top_musicas[released_year][3]:
        top_musicas[released_year] = musica

# Criar lista ordenada das músicas mais tocadas por ano
top_musicas_lista = [top_musicas[ano] for ano in sorted(top_musicas.keys())]

# Exibir o resultado final
for item in top_musicas_lista:
    print(item)
