import json
import model

# .load decodes the JSON object
# parser to seed database 
def load_cards(db_session):
	with open('JOU.json') as f:
		data = json.load(f)
        # data for Cards Table
		card_array = data['cards']
		for card in card_array:
			name = card['name']
			spellTypes = card['type']
			rarity = card['rarity']
			print " I am %s type: %s rarity: %s" % (name, spellTypes, rarity)

			card_data = model.Card(name = name, spellTypes = spellTypes, rarity = rarity)
			db_session.add(card_data)


def main(db_session):
	load_cards(db_session)
	db_session.commit()

if __name__ == "__main__":
	s = model.db_session
	main(s)