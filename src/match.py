from PIL import Image
import imagehash

user_url = ''
user_hash = imagehash.pHash(Image.open(user_url))
target_url = ''
target_hash = imagehash.pHash(Image.open(target_url))