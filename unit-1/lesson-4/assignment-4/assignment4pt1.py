import sys
import random
from PIL import Image
### 1)
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

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):
# ### think abt it changing the grid along x-axis and y-axis
# ### regular, colors are blue and red, making y negative is only red
# ### this means that the numbers affects position and color... both negatives makes no color at all, negative x makes only blue
#         pixel = (x % -255, 0, y % 200)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

##########

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):
# ### along y axis for how along y the image is manipulted
#     for x in range(400):
# ### this is along x axis and is basically the area of the manipulated image
#         r = 0
#         #### idk
#         b = 0
#         #### idk
#         if x % 50 == 0:
#             ### changing first # made more or less color lines along x axis
#                     ### but changing second # manipulates the spacing between the lines somehow, but still dependent on amount of lines along x
#        #if x % 2 == 0:
#        ### this made a lot of blue lines!   
            
#             b = 400
#             #### this # is saturation???
#     ### ok so this for loop is basically saying for x along these parts, making it a pattern with the modulus, the pixels there are blue
#         if y % 20 == 0:
#             ### same thing for x but along y with the first # manipulating how many lines dependent on modulus
#             r = 255
#             ### this # also still manipulates x axis???

#         if y % 30 == 0:
#         ### this makes another y axis which is why it's like a stripe
#             r = 255
#             b = 255
#             ### these # somehow manipulate the color of the lines but im not too sure how

#         pixel = (r, 0, b)
#                 ### so changing middle # is basically adding green to pixel or image
#        #pixel = (r, 100, b)
#        ### this made it green!
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

#####################################
#####################################
#####################################


