import requests
import pprint

artist = "titas" # Ex.: titas, u2

title = "epitafio" # Ex.: epitafio, one


endpoint = f'https://api.lyrics.ovh/v1/{artist}/{title}'


response = requests.get(endpoint)

# Removendo os caracteres \n e \r

lyrics = response.json()["lyrics"].replace("\r", "") #.replace("\n", " ")

pprint.pprint(lyrics)

# Salvando a letra em um arquivo texto
filename = f"{artist}_{title}.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(lyrics)