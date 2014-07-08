import sqlite3

class Card_Lib(object):
	"""Corresponds to attributes in the mtgJSON object"""
	def __init__(self, name, spell_type, imageName):
		self.name = name
		self.spell_type = spell_type
		self.imageName = imageName