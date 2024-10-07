###### algorithm I - shadows
#### first import libraries!!!!
### for using path to get images
from os import listdir, path
### import random for naming images, and using random functions to pull random images!!!
import random
###  import PIL for images stuff!!
from PIL import Image
### import sys to use user input arguments for code to work
import sys

###########################

######## start of code ––
### some error handlingggg
if len(sys.argv) !=2:
    exit("you need to pick and choose a folder! what's gonna happen?!?")

########## how to get a random image a specific folder... changing into inputing specific folder on command line tho-
### so the variable will be the all files in folder that is inputted
files = listdir (sys.argv[1])
files.remove(".DS_Store")
    
### names random images and uses random library to choose a random image from inputted folder!!!
random_img1 = random.choice(files)
# random_img2 = random.choice(files)

#### now open random images
img = Image.open( path.join(sys.argv[1],random_img1) )

#### always resize!
image1 = img.resize((300,200)).convert("RGBA")

##### makes a new image with a backdrop ...
new_image = Image.new( "RGBA", (600,425), "black" )

### pastes first image 
new_image.paste( image1,(150,10) )


####### now to make the shadow image

## so making a copy of random image AND using .transpose which flips/mirrors the image, making the shadow
img1 = image1.copy().transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)

#### using alpha to add transparency
img1.putalpha(128)

## need to make it transparent to be a realll shadow!
new_image.alpha_composite( img1, (150, 210))

##### finally adding shadow to complete image
# new_image.paste( img1, (150,210) )

#### save the resulting image, and use random to help with names
randomnumberforimage = int(random.random() * 100)
new_image.convert("RGB").save("shadow" + str(randomnumberforimage)+ ".jpg")
new_image.show(new_image)













