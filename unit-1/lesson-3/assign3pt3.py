## 3)
import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This command requires two arguments: the name of two image files")

## this order is right dont change
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
## similar to rotate() this will blend them!
blended_img = Image.blend(img1,img2,.5)

blended_img.save("blended.jpg")
