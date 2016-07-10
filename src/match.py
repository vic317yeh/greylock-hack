from PIL import Image
import imagehash
import os

DIFFERENCE_BAR = 10

def match(userImgSrc, targetImgSrc)
	user_img = Image.open(userImgSrc)
	target_img = Image.open(targetImgSrc)
	user_hash = imagehash.average_hash(user_img)
	target_hash = imagehash.average_hash(target_img)
	result = True if user_hash-target_hash <= DIFFERENCE_BAR else False
	return result

