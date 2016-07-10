from PIL import Image
import imagehash
import os

DIFFERENCE_BAR = 10

def match(userImgSrc, targetImgSrc)
	basedir = os.path.dirname(os.path.realpath(__file__))
	userImgSrc = '6.JPG'
	targetImgSrc = '7.JPG'
	user_img = Image.open(basedir + '/../static/img/' + userImgSrc)
	user_hash = imagehash.average_hash(user_img)
	target_img = Image.open(basedir + '/../static/img/' + targetImgSrc)
	target_hash = imagehash.average_hash(target_img)

	if user_hash-target_hash <= DIFFERENCE_BAR:
		return True
	else:
		return False
