file = open("hamlet.txt" , "r") 

word_counts = {}
#### for this dictionary it will be key - word and value - frequency

#### line is a variable and im saying that for the lines in the text from my other variable called file
for line in file:
    ### for each line, split each word to be its own key
    for word in line.split():
                #### helpful method that splits whole things up! so think about a sentence as a string, a whole, and .split() will split the string into substrings, so the sentence will be split into words
        # print(word)
        #### it's working so far!!!!!
        # word_counts = {word}
        # print("the word:" , word_counts)

##### if word is in word_counts, add 1 to frequency
# for word in word_counts:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
##### else word is not in word_counts, add to word count as 1
        else:
            word_counts[word] = 1
        
allPairs = iter((word_counts.items()))
            ### iter is a function for returning the iterator / think of it like repeating the sequence of something, in order but one at a time, it allows you to get back the next thing in a list one at a time in order

firstPair = next(allPairs)
mostFrequent = firstPair[0]
# print(mostFrequent)
for word in word_counts:
    if word_counts[word] > word_counts[mostFrequent]:
        mostFrequent = word

print("the most frequent word is:",mostFrequent,"!!! " "it appears", word_counts[mostFrequent], "times!!!!" )
# for counts in word_counts.items():

        

