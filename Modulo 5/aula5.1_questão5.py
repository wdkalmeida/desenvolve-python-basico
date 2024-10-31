

import emoji

# Dicionário de emojis disponíveis para o usuário
emojis_disponiveis = {
    ":grinning_face:": emoji.emojize(":grinning_face:"),
    ":thumbs_up:": emoji.emojize(":thumbs_up:"),
    ":red_heart:": emoji.emojize(":red_heart:"),
    ":smiling_face_with_sunglasses:": emoji.emojize(":smiling_face_with_sunglasses:"),
    ":winking_face:": emoji.emojize(":winking_face:"),
    ":face_with_tears_of_joy:": emoji.emojize(":face_with_tears_of_joy:")
}

# Exibe a lista de emojis disponíveis com seus códigos
print("Emojis disponíveis:")
for codigo, emoji_visivel in emojis_disponiveis.items():
    print(f"{codigo} -> {emoji_visivel}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase usando os códigos de emoji acima (ex.: Olá :winking_face:!): ")

# Decodifica a frase com os emojis e exibe
frase_emojizada = emoji.emojize(frase_codificada)
print("\nFrase com emojis:")
print(frase_emojizada)
