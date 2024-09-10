### 1)
from unit1lesson2 import *
smallest_number = number_list[0]
# the variable "smallest_number" is saying that the first number in number_list is the smallest number
if number_list[1] < smallest_number:
# the "if" statement is making a comparison between the smallest number that was named the first number in the list with the second number in the list    
    smallest_number = number_list[1]
# the variable smallest_number will now be the second number in the number list, only if it meets the if condition
for num in number_list:
# this is starting a loop with each number, which is the variable num, in number_list
    if num < smallest_number:
    # with if it sets another condition where each item in the number_list is set to be compared with smallest_number and if it meets the if condition it will become smallest_number
            smallest_number = num
            #saying now that smallest_number will become variable num
print (smallest_number)
### 1) 175


### 2)
from unit1lesson2 import *
smallest_number = number_list[0]
## saying here again that the first value in number list is the smallest number
if number_list[1] < smallest_number:
## if statement to compare the values to find the actual smallest number
    smallest_number = number_list[1]
## now after comparing the smallest number would become new smallest number if it satisfies if statement
for x in number_list:
    ## now this starts a for loop saying to repeat the comparison, but with more conditions
     if 500 < x < smallest_number:
          ## another condition to satisfy with if statement; the condition states that the smallest number must be greater than x which must be greater than 500, making 500 the real smallest number
          smallest_number = x
## so smallest number will be x when if statement is satisfied which makes the loop, also realized that order matters here
print(smallest_number)
### 2) 501




### 3)
from unit1lesson2 import *
smallest_number = number_list[0]
## again beginning with a variable saying that the smallest_number is the first value in the number_list
if number_list [1] < number_list[0]:
     ## an if statement that says if the second item in number_list is smaller than the first item
     smallest_number = number_list[1]
     ## the if condition is met then the smallest_number will become the second item in number_list
for num in number_list:
     ## starting a loop to continue comparing the items in list to find the smallest number
     if num < smallest_number and num % 2 == 0:
          ## this took me the longest and was so hard to figure out, but i kept thinking how the number needed to be even, which meant another condition had to be met
          ## i didn't realize i could write two conditions and that i could use "and" in code, but the if statement is that if the num or any item in the number_list is smaller than the current number and it is even, or that the remainder is 0
          smallest_number = num
          ## the condition is met and it will become the smallest numb
print(smallest_number)
### 176



###4
from unit1lesson2 import *
last_word = word_list [0]
## so last_word is a variable and it's saying that the last_word is the first item in the list
for word in word_list:
     ## word as a variable for all words in the list, making a loop to continue comparing
     if word > last_word:
          ## computer knows the alphabet, so if the word in the list is greater than what's made the last_word, which is the first item in the list
          last_word = word
          ## if condition satisfied and the word in the list will become the new last_word
print(last_word)
### violation



###5
from unit1lesson2 import *
longest_word = word_list[0]
## variable longest_word is the first item in word_list 
if len(word_list[1]) > len(word_list[0]):
     ## using len() to find length of words and compare the first item in list to second, 
     longest_word = word_list[1]
     ## the longest_word in the list becomes the second item when the if condition is met, if the second word is longer than the first
     ## now using for to make a looooop
for lw in word_list:
     ## lw is for all words or items in word_list
     if len(lw) > len(longest_word):
          ## saying that if the length of any word in the list is longer than the second item
          longest_word = lw
          ## if the if statement is satisfied then the length of whatever word in the list will be longest and will become the longest_word
print(longest_word)
### rehabilitation