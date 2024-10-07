import os
import random
from PIL import Image

### new system, "os" ?

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
###########################    ALGO1 BUT WITH 2 RANDO IMGS
#### take random photo and opens them ?????
########## how to get a random image a specific folder... changing into inputing specific folder on command line tho-

# files = listdir (sys.argv[1])
# files.remove(".DS_Store")

# # ########## some error handlingggg
# # if len(sys.argv) !=2:
# #     exit("pick and choose a folder! what's gonna happen?!?")
    
# ### name random images!!!
# random_img1 = random.choice(files)
# random_img2 = random.choice(files)

# #### now open random images
# img1 = Image.open( path.join(sys.argv[1],random_img1) )
# img2 = Image.open( path.join(sys.argv[1],random_img2) )

# #### always resize!
# image1 = img1.resize((300,200)).convert("RGBA")
# image2 = img2.resize((300,200)).convert("RGBA")


# ##### makes an image with maybe a backdrop ig...
# new_image = Image.new( "RGBA", (600,425), "blue" )

# ### pastes first image 
# new_image.paste( image1,(150,10) )


# # ####### now to make the shadow image
# # ## so making a copy of random image AND using .transpose which flips/mirrors the image, making the shadow
# shadow = image2.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)

# shadow.putalpha(128)


# # ## need to make it transparent to be a realll shadow!
# new_image.alpha_composite( shadow, (150, 210))

# ##### finally adding shadow to complete image
# new_image.paste( shadow, (150,210) )



# #### save the resulting image
# randomnumberforimage = int(random.random() * 100)
# new_image.convert("RGB").save("shadow" + str(randomnumberforimage)+ ".jpg")
# new_image.show(new_image)















###### THIS WAS FROM geeksforgeeks.org

import os
import random

# # def get_random_image_path(folder_path):
# #     try:
# #         files = os.listdir(folder_path)
# #         # Filter the list to get only image files
# #         images = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# #         if not images:
# #             print("No images found in the specified folder.")
# #             return None

# #         # Choose a random image file
# #         random_image = random.choice(images)
# #         random_image_path = os.path.join(folder_path, random_image)
# #         return random_image_path
      
# #     except Exception as e:
# #         print(f"An error occurred while selecting image randomly: {e}")
# #         return None

# # def display_image(image_path):
# #     try:
# #         if image_path and os.path.isfile(image_path):
# #             with Image.open(image_path) as img:
# #                 img.show()
# #                 print(f"Displayed image: {image_path}")
# #         else:
# #             print(f"Invalid image path: {image_path}")
# #     except Exception as e:
# #         print(f"An error occurred while displaying the image: {e}")

# # def show_random_image_from_folder(folder_path):
# #     random_image_path = get_random_image_path(folder_path)
# #     display_image(random_image_path)

# # # usage:
# # # if __name__ == "__main__":
# # #     folder_path = "images-0"
# # #     if os.path.isdir(folder_path):
# # #         show_random_image_from_folder(folder_path)
# # #     else:
# # #         print(f" The specified folder does not exist: {folder_path}")


# # import os
# # import random
# # import sys 

# # # Get a list of image files in a directory
# # image_directory = '/Users/kirstenbaraoidan/cla24/unit-1/final-project/' + sys.argv (2)
# # image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

# # # Randomly select an image file
# # random_image = random.choice(image_files)

# # # Construct the full path to the image
# # random_image_path = os.path.join(image_directory, random_image)

# # # print(random_image_path)

# width = 100
# height = 100

# img = Image.new("RGB", (width,height), (255,255,255) )

# # loop 500 times, and each time, pick a random x and a random y
# # and draw a pixel there
# for n in range(750):
    
    
#     # even distribution
#     x = int( random.random() * 100 )
#     y = int( random.random() * 100 )

#     # ## gaussian distribution
#     # x = int( random.gauss(50,50) )
#     # y = int( random.gauss(100,100) )

# #     # gaussian distribution just for x
# #     ## making pixels in this range and distribution isn't across whole image
# #     x = int( random.gauss(50,10) )
# #     y = int( random.random() * 100  )

#     img.putpixel( (x,y), (0,0,0) )

# img.save("more-rando-gauss-x.png")
# img.show()



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
image1 = img.resize((67,67)).convert("RGB")

### then make new image to put it on
width = 100
height = 100
new_image = Image.new( "RGB", (width,height), (255,255,204) )

### paste random image!!!
###### (100,100) is so center
new_image.paste(image1, (25, 25))

###### then add confetti!! so use even distribution to make random pixels

### so the number is to loop (for loop) how much there would be, if lower there'll be less and higher more, a for loop to make green
for n in range(750):
    
    ### even distribution
    ######## so think of it as area of the image it will cover, so it's 600 for both so it will cover the whole area, but if decreased, it won't cover some area
    x = int( random.random() * 100 )
    y = int( random.random() * 100 )

###### .putpixel is like pasting pixels or adding them into the new image, and adding color! this is for greeeeen
    new_image.putpixel( (x,y), (0,255,0) )

### another even distribution to add more, but a for loop to make blue!
for l in range(750):
    
    ######## so think of it as area of the image it will cover, so it's 200 for both so it will cover the whole area, but if decreased, it won't cover some area
        ### even distribution
    x = int( random.random() * 100 )
    y = int( random.random() * 100 )

    new_image.putpixel( (x,y), (0,0,255) )

### one last for loop with an even distribution to make red!
for h in range(750):

    ## even distribution
    x = int( random.random() * 100 )
    y = int( random.random() * 100 )    

    new_image.putpixel( (x,y), (255,0,0) )

#### now resize whole image
new_img = new_image.resize((600,600))





### using random library again to help with names, saving and showing image so you see what you made!
randomnumberforimage = int(random.random() * 100)
new_img.save("partytime" + str(randomnumberforimage) + ".jpg")
new_img.show()


