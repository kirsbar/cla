### doing same as markov-lib but using no library
### a dumber version of markovify
import random
import sys
import pprint
### new library called prettyprint "pprint" which will help print dictionaries better, makes things more legible in terminal

filename = sys.argv[1]
text = open(filename).read().lower().split()
markovDictionary = {}	



# use this function to get indexes for words
def getIndexForWord(wordFromLoop, nextPossibleWordsAmount): 
    possibleWordIndexes = []
    allWords = []
    for index, word in enumerate(text):
        if word == wordFromLoop:
            possibleWordIndexes.append(index)
    # print(wordFromLoop, "indexes:", possibleWordIndexes)
    return possibleWordIndexes[nextPossibleWordsAmount]


#### *markov : looks at words, looks up words that could possibly come next, randomly chooses one of next words when generating a text ; looking up next probable word and generating text based on that probability after making model of given text


# build dictionary
totalWords = len(text)
for word in text:
    if not word in markovDictionary:
        markovDictionary[word] = []

    if text.index(word) == (totalWords - 1): break

    nextPossibleWordsAmount = len(markovDictionary[word]) 
    textIndex = getIndexForWord(word, nextPossibleWordsAmount)

    if word == text[(totalWords - 1)]:
        continue
    else:
        nextWord = text[textIndex + 1]
        markovDictionary[word].append(nextWord)

# pprint.pprint(markovDictionary)
# print(markovDictionary)




# generate text from dictionary
chosenWord = random.choice(text)
generatedText = []
for i in range(80):
    if chosenWord == text[(totalWords - 1)]:
        chosenWord = text[0]
    else:
        generatedText.append(chosenWord)
        nextWord = random.choice(markovDictionary[chosenWord])
        chosenWord = nextWord

finalPrintOut = " ".join(generatedText)

print("\n\n\n")
print(finalPrintOut)
print("\n\n\n")
###### !!!! extremely slow if the text file is huge. so if using books, maybe find short stories for workshopping and testing code!!!!