import sys
from PIL import Image

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# data = []
# ### this determines kinda the gradient, cant be >100
# for i in range(100):
#     pixel = (i, 0, 0)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])

##########

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):
### think abt it changing the grid along x-axis and y-axis
### regular, colors are blue and red, making y negative is only red
### this means that the numbers affects position and color... both negatives makes no color at all, negative x makes only blue
        pixel = (x % -255, 0, y % 200)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])