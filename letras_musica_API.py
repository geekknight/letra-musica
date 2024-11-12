import requests
import pprint

artist = "titas" # Ex.: titas, u2

title = "epitafio" # Ex.: epitafio, one

# Source of lyrics.ovh and API to search for lyrics of a song
endpoint = f'https://api.lyrics.ovh/v1/{artist}/{title}'


response = requests.get(endpoint)

# Removing the characters \n e \r
lyrics = response.json()["lyrics"].replace("\r", "") #.replace("\n", " ")

pprint.pprint(lyrics)

# Saving the lyrics to a text file
filename = f"{artist}_{title}.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(lyrics)