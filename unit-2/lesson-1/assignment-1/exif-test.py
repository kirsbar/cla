from os import listdir, path
from PIL import Image, ExifTags
#######
### adding sys.argv so user can use this with inputting own image
import sys 
### okay i messsed with this a bit but finally worked! allows me to choose the image and input it on terminal with arguments
if len(sys.argv) !=2:
    exit("add the name of an image from imgaes folder!!!")
files = listdir("images")
image = sys.argv[1]
#######
img = Image.open(path.join("images", image))
exifData = img.getexif()

print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])