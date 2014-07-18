
from PIL import Image
import hashlib 

def load_img():
	image1 = Image.open("JOU_imgs/Font_Of_Ire.png")
	image2 = Image.open("JOU_imgs/Hypnotic_Siren.png")
	image1.show()
	image2.show()
	return image1, image2


#makes image grayscale
def make_gray(image1, image2):
	imageG1 = image1.convert('L')
	imageG2 = image2.convert('L')
	imageG1.show()
	imageG2.show()

	return imageG1, imageG2

#makes img 8X8
def make_small(imageG1, imageG2):
	small1 = imageG1.resize((8, 8), Image.BICUBIC)
	small2 = imageG2.resize((8, 8), Image.BICUBIC)
	small1.show()
	small2.show()
	return  small1,  small2

#calculates the hash
def hash_img(small1, small2):
	hashimg1 = hash('small1')
	hashimg2 = hash('small2')
	print hashimg1
	print hashimg2
	return hashimg1, hashimg2

def compare(hashimg1, hashimg2):
	if hashimg1 == hashimg2:
		print True
	else:
		print False

def main():
	loaded = load_img()
	gray = make_gray(loaded)
	small = make_small(gray)
	hashimg = hash_img(small)
	compare = compare(hashimg)

if __name__ == "__main__":
	main()
