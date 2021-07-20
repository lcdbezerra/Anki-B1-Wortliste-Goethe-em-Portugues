import json

# filepath = "deck.json"
filepath = "/home/camaral/Documents/anki_export/B1_Wortliste_DTZ_Goethe/deck.json"

with open(filepath) as f:
	data = json.load(f)

notes = data["notes"]

fields = notes[0]["fields"]

breakpoint()