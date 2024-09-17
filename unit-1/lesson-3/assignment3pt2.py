## 2)
import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This command requires two arguments: the name of an image file")

## this order is right dont change
img = Image.open( sys.argv[1] )
rotated_img = img.rotate( int(sys.argv[2]) )

rotated_img.save("rotated-" + sys.argv[1])
print("You typed the filename: " + sys.argv[1] )
print("This is a " + img.format)
print(img.format_description)
print("Size: " + str(img.size) )
