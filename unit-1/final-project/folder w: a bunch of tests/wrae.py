from os import listdir, path
import random
from PIL import Image
import sys

files = listdir (sys.argv[1])
files.remove(".DS_Store")

random_file = random.choice(files)

# img = Image.open( path.join("images",random_file) )