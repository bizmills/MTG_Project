import json
import model
import os
import glob
import time
from PIL import Image
import imagehash


# .load decodes the JSON object
def load_cards(db_session):
	with open('M15.json') as f:
		data = json.load(f)
        # data for Cards Table
		card_array = data['cards']
		for card in card_array:
			name = card['name']
			spellTypes = card['type']
			rarity = card['rarity']
			imageName = card['imageName']
			sets_id = 1
			print imageName
			# print " I am %s type: %s rarity: %s" % (name, spellTypes, rarity)

			card_data = model.Card(name = name, spellTypes = spellTypes, rarity = rarity, sets_id = sets_id, imageName = imageName)
			db_session.add(card_data)
			db_session.commit()
			db_session.refresh(card_data)

		# return card_data 


def hash_cards(db_session):
	my_images_path = "MTGimglib/set/M15" #put your image path here if you want to override current directory
	extension = "*.jpg"

	if not my_images_path:
	    path = os.getcwd() #get the current directory
	else:
	    path = my_images_path

	imgs = list() #load up an image list
	directory = os.path.join(path, extension)
	print directory
	files = glob.glob(directory)

	for file in files:
		img = Image.open(file)
		imageG = img.convert('L')
		small = imageG.resize((9, 8), Image.ANTIALIAS)
		#img hash
		hashimg = imagehash.dhash(small)
		#change to number
		h = str(hashimg)
		num_of_bits = 8
		hashbin = bin(int(h, 16))[2:].zfill(num_of_bits) # backfills 0s 
		#get file name
		name_split = file.split('/')
		img_name = name_split[-1]
		name_ex = img_name.split('.')
		card_name = name_ex[0]

		# import pdb; pdb.set_trace()
		# need to handle exceptions
		card_from_table = db_session.query(model.Card).filter_by(imageName=card_name).update({'hashId': hashbin})
		db_session.add(card_from_table)
		db_session.commit()
		db_session.refresh(card_from_table)


		print hashbin


def main(db_session):
	cards_loaded = load_cards(db_session)

	hash_loaded = hash_cards(db_session)



if __name__ == "__main__":
	s = model.db_session
	main(s)