
from PIL import Image
import hashlib 
import imagehash

def load_img():
	image1 = Image.open("test_scan/inferno fist.png")
	image2 = Image.open("test_scan/test_inferno_fistcropped.png")

	return image1, image2


#makes image grayscale
def make_gray(image1, image2):
	imageG1 = image1.convert('L')
	imageG2 = image2.convert('L')

	print type(imageG1)
	print dir(imageG1)

	return imageG1, imageG2

#makes img 9X8
def make_small(imageG1, imageG2):
	small1 = imageG1.resize((9, 8), Image.ANTIALIAS)
	small2 = imageG2.resize((9, 8), Image.ANTIALIAS)

	return  small1, small2

#calculates the hash
def hash_img(small1, small2):
	hashimg1 = imagehash.dhash(small1)
	hashimg2 = imagehash.dhash(small2)
	print hashimg1
	print hashimg2
	return hashimg1, hashimg2

def compare(hashimg1, hashimg2):
	print hashimg1 == hashimg2
	return hashimg1 == hashimg2

def hash_to_bin(hashimg1, hashimg2):
	h1 = str(hashimg1)
	h2 = str(hashimg2)
	num_of_bits = 8
	hashbin1 = bin(int(h1, 16))[2:].zfill(num_of_bits) # backfills 0s 
	hashbin2 = bin(int(h2, 16))[2:].zfill(num_of_bits)
	print hashbin1
	print hashbin2
	return hashbin1, hashbin2

def ham_dist(hashbin1, hashbin2):
	diffs = 0
	for ch1, ch2 in zip(hashbin1, hashbin2):
		if ch1 != ch2:
			diffs += 1
	print diffs
	return diffs

# def is_similar(diffs):
# 	if diffs <= 5:
# 		same = True
# 	else:
# 		same = False
# 	print same
# 	return same

def main():
	loaded1, loaded2 = load_img()
	gray1, gray2 = make_gray(loaded1, loaded2)
	small1, small2 = make_small(gray1, gray2)
	hashimg1, hashimg2 = hash_img(small1, small2)
	# s = str(hashimg1)
	# print type(s), s
	result = compare(hashimg1, hashimg2)
	hashbin1, hashbin2 = hash_to_bin(hashimg1, hashimg2)
	diff = ham_dist(hashbin1, hashbin2)
	# same = is_similar(diffs)

if __name__ == "__main__":
	main()
