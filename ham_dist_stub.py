from flask import Flask, request, session, render_template, g, redirect, url_for, flash
from model import db_session, Card, Collection, Collection_item, User, Set
import jinja2
import tempfile
import base64
from PIL import Image, ImageChops
import imagehash
import sqlalchemy 
from sqlalchemy import orm

def hash_scan():
	img = Image.open("test_scan/test_inferno_fistcropped.png")
	imageG = img.convert('L')
	small = imageG.resize((9, 8), Image.ANTIALIAS)
	hashimg = imagehash.dhash(small) # hash img
	hstr = str(hashimg) # change to number
	num_of_bits = 64
	hashbin = bin(int(hstr, 16))[2:].zfill(num_of_bits)
	print hashbin
	return hashbin

def clean_str():
	db_imgs = []	
	stored_imgs = db_session.query(Card.hashId).select_from(Card).all()
	for image in stored_imgs:
		new_string = str(image[0])
		db_imgs.append(new_string)
	return db_imgs

def ham_dist(hashbin, db_imgs):
	poss_cards = [] # TO DO append the possible cards
	for image in db_imgs:
		diffs = 0
		while diffs <= 10:
			for ch1, ch2 in zip(image, hashbin):
				if ch1 != ch2:
					diffs += 1
			if diffs <= 10: 
				poss_cards.append(image)
	# remove the "None"s from the list
	matches = filter(lambda a: a != 'None', poss_cards)
	# get the card name associated with each hash
	import pdb; pdb.set_trace()	
	match_name = []
	n = 0
	your_card = db_session.query(Card).filter_by(hashId = str(matches[n])).all()[n].name
	for match in your_card:
		match_name.append(your_card)
		n += 1
	print match_name


def main():
	hashed = hash_scan()
	clean = clean_str()
	match = ham_dist(hashed, clean)


# """Once more with feeling"""
# def flip_bits(hashbin):

	# write something that creats a list of all the variant strings



if __name__ == "__main__":
	main()


# stuff to returm card name of matched
	#db_session.query(Card).filter_by(hashId = str(matches[0])).all()[0].name