## 1)
import sys
## hint
#from unit1lesson2 import word_list
word_list = sys.argv
## this is saying that the word list that will be alphabetized are the arguments
word_list.pop(0)
## .pop() so only user inputs are used
## argument has to be 1 so it doesn't include assignment name
sortedlist = sorted(word_list)
## using sort function to alphabetize the words given in command line, or to alphabetize the arguments that are from the word list
print (sortedlist)


# last_word = sys.argv [0]
# ## so last_word is a variable and it's saying that the last_word is the first item in the list
# if sys.argv [1] > sys.argv [0]:
#     last_word = sys.argv [1]
# for word in word_list:
#      ## word as a variable for all words in the list, making a loop to continue comparing
#      if word > last_word:
#           ## computer knows the alphabet, so if the word in the list is greater than what's made the last_word, which is the first item in the list
#           last_word = word
#           # if condition satisfied and the word in the list will become the new last_word

# for word in word_list:
#     if sys.argv[0] < sys.argv[1]:

#     print(word_list)