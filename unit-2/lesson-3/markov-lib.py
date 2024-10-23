### this takes a text file...
import markovify
# # look at documentation for markofivy here: https://github.com/jsvine/markovify

text = open("dorian_gray.txt").read()

generator = markovify.Text(text, state_size=3) 

### empty paragraph variable and passing short length into that empty variable 
paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(100))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

### sometimes returns none if the text file is too small
### think about data not working or code not working with data