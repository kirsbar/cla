##### algorithm II - make anything a party! (adds confetti!!!)
### first import librariessss!
from os import listdir, path
import sys
from PIL import Image
import random

########################
##### start of code ––
### some errorrrr handling
if len(sys.argv) !=2:
    exit("add a folder and see what happens!! ;)")
### opening/choosing random photos from command lineeeee from folders
files = listdir(sys.argv[1])
# files.remove(".DS_Store")

random_img = random.choice(files)

### code that opens image and manipulates (resize)
img = Image.open( path.join(sys.argv[1],random_img) )
image1 = img.resize((400,400)).convert("RGB")

### then make new image to put it on
width = 600
height = 600
new_image = Image.new( "RGB", (width,height), (255,255,204) )

### paste random image!!!
###### (100,100) is so center
new_image.paste(image1, (100, 100))

###### then add confetti!! so use even distribution to make random pixels
### so the number is to loop (for loop) how much there would be, if lower there'll be less and higher more, a for loop to make green
for n in range(2000):
    
    ### even distribution
    ######## so think of it as area of the image it will cover, so it's 600 for both so it will cover the whole area, but if decreased, it won't cover some area
    x = int( random.random() * 600 )
    y = int( random.random() * 600 )

###### .putpixel is like pasting pixels or adding them into the new image, and adding color! this is for greeeeen
    new_image.putpixel( (x,y), (0,255,0) )

### another even distribution to add more, but a for loop to make blue!
for l in range(2000):
    
    ######## so think of it as area of the image it will cover, so it's 200 for both so it will cover the whole area, but if decreased, it won't cover some area
        ### even distribution
    x = int( random.random() * 600 )
    y = int( random.random() * 600 )

    new_image.putpixel( (x,y), (0,0,255) )

### one last for loop with an even distribution to make red!
for h in range(2000):

    ## even distribution
    x = int( random.random() * 600 )
    y = int( random.random() * 600 )    

    new_image.putpixel( (x,y), (255,0,0) )

### using random library again to help with names, saving and showing image so you see what you made!
randomnumberforimage = int(random.random() * 100)
new_image.save("partytime" + str(randomnumberforimage) + ".jpg")
new_image.show()

