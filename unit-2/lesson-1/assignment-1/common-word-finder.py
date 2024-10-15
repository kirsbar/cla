# file = open("hamlet.txt" , "r")
# ### this is a dictionary 
# word_counts = {}

# ### for each line in hamlet
# for line in file:
#     ### for each word in each line in hamlet
#                     ### .split() very helpful! it takes a string and splits it into more substrings! so splits a sentence into its individual words essentially
#     for word in line.split():
#     ##### if word is in word_counts, add 1 to frequency
#         if word in word_counts:
#             word_counts[word] = word_counts[word] + 1
        
#         ##### else word is not in word_counts, add to word count as only 1
#         else:
#             word_counts[word] = 1    

# #### making a variable for the pairs/tuples
# allPairs = iter((word_counts.items()))
#             ### iter is a function for returning the iterator / think of it like repeating the sequence of something, in order but one at a time, it allows you to get back the next thing in a list one at a time in order

# Pair = next(allPairs)
# # for items in word_counts.items():
# #     # items = sorted(word_counts)
# #     print(items)
# # l = sorted(word_counts.items())

# mostFrequent1 = Pair[0]
# for word in word_counts:
#     if word_counts[word] > word_counts[mostFrequent1]:
#         mostFrequent1 = word
# ### mostFrequent1 = "the" : 141

# print("the first most frequent:", mostFrequent1, "\nit appears", word_counts[mostFrequent1], "times!")
# ####### !!! this is from stackoverflow!!! so i needed help to sort the dictionary but sort by values specifically
# ### so new variable for the sorted dictionary, it will be based on key-value pairs and looking at the values
# sorted_word_counts = {key: value for key, value in 
# sorted(word_counts.items(), key = lambda item: item[1])}
# ### using sorted() and .items() to individually go thru each item's value in the dictionary
# ### lambda is a function, don't really understand it tbh but to try, its for the sorted() function and acts as the key argument
# print("these are the words:", sorted_word_counts)
###### top 10 words in hamlet: "the', "and", "of", "to", "I", "in", "my", "it", "a", "not" 

########################################################

###### skip over common words (using top 5 words)

file = open("hamlet.txt" , "r")
# ### this is a dictionary 
word_counts = {}
common_words = ["the", "and", "of", "to", "I"]

### for each line in hamlet
for line in file:
    ### for each word in each line in hamlet
    for word in line.split():
        ### if the word is in the common_words list
        ## if word in common_words:
            ## words = common_words.pop(0)
            ##### tried .pop() but it's for the index! and don't really know that so no
        ##    del common_words
            ##### tried using del to delete the whole list but i'm realizing i have the right idea but i'm doing it wrong, so i'll try flipping it
        # if word in word_counts:
        #     del word_counts[common_words]
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        
        ##### else word is not in word_counts, add to word count as only 1
        else:
            word_counts[word] = 1    

######### basically added this section to previous code
##### this finally worked!!!
### okay so i did in fact get this from google but it's basically what i was thinking but just flipped
### so again making the variable "word" mean any word from the list of common words
for word in common_words:
    ### if the word is also in the dictionary
    if word in word_counts:
        ### delete those words in the common words list from the whole dictionary
        del word_counts[word]
##########

allPairs = iter((word_counts.items()))
            
Pair = next(allPairs)
# for items in word_counts.items():
#     # items = sorted(word_counts)
#     print(items)
# l = sorted(word_counts.items())

mostFrequent1 = Pair[0]
for word in word_counts:
    if word_counts[word] > word_counts[mostFrequent1]:
        mostFrequent1 = word
### mostFrequent1 = "the" : 141


print(word_counts)
print("the most frequent word that isn't common:", mostFrequent1, "!!!")
#### more interesting (but kinda not really) most frequent word: "in" appearing 65 times