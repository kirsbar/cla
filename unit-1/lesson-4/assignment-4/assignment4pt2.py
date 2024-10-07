### 2)
import sys
from PIL import Image

if len(sys.argv) != 5:
    exit("This program requires four arguments: the name of four image files to combine.")

# ###### overlaying 4 images
# ### first open the images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )
# img3 = Image.open( sys.argv[3] )
# img4 = Image.open( sys.argv[4] )

# ### next resize  images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )
# img3.thumbnail( (400,400) )
# img4.thumbnail( (400,400) )


# # make a new image 600x600, with a white background
# new_image = Image.new( "RGB", (600,600), "white" )

# # paste in the first image to the upper-left corner (0,0)
# new_image.paste(img1, (0,0) )

# ### paste in the the next images
# new_image.paste(img2, (20, 20) )

# new_image.paste(img3, (145,145) )

# new_image.paste(img4, (40,2) )

# # # save the resulting image
# new_image.save("overlay_images.jpg")


########## blennnddd

# # ### first open the images
# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )
# img3 = Image.open( sys.argv[3] )
# img4 = Image.open( sys.argv[4] )

# ### next resize  images so they are no bigger than 400x400
# # but preserve the original aspect ratio
# img1.thumbnail( (400,400) )
# img2.thumbnail( (400,400) )
# img3.thumbnail( (400,400) )
# img4.thumbnail( (400,400) )

# new_image = Image.new( "RGB", (600,600), "white" )

# img2.putalpha(128)
# img3.putalpha(225)
# img4.putalpha(45)

# new_image.alpha_composite(img2, (0,0) )
# new_image.alpha_composite(img3, (0,0) )
# new_image.alpha_composite(img4, (0,0) )
# new_image.convert("RGB").save("new.png")

#### this was not working at all and I really struggled to figure it out :(



# 3
# if len(sys.argv) != 5:
#     exit("This program requires 4 arguments: the name of 4 image files to combine.")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )
img4 = Image.open( sys.argv[4] )

img1.thumbnail( (200, 200) )
img2.thumbnail( (200, 200) ) 
img3.thumbnail( (200, 200) )
img4.thumbnail( (200, 200) )

new_image = Image.new( "RGBA", (200, 200), "black" )

new_image.paste(img1, (0,0) )

img2.putalpha(120)
img3.putalpha(90)
img4.putalpha(100)

new_image.alpha_composite(img2, (0,0) )
new_image.alpha_composite(img3, (0,0) )
new_image.alpha_composite(img4, (0,0) )

new_image.save("collaging1-saved-for-demo.png")
