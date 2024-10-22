### new libraries!!!
import requests
from bs4 import BeautifulSoup
import markovify

### so to webscrap using requests and .get to get all the text from this link i put in
response = requests.get("https://www.nationalgeographic.com/animals/birds/facts/penguins-1")
                    ### https://www.cgdev.org/publication/2022-global-refugee-work-rights-report
                    ### https://www.wikihow.com/Make-a-Halloween-Costume
                    ### https://sheepandstitch.com/how-to-knit/
                    ### 
## some links blocked me and interesting how the text made was telling me that im blocked :(
    ##### https://www.cgdev.org/publication/2022-global-refugee-work-rights-report
    ##### https://www.cgdev.org/publication/2022-global-refugee-work-rights-report
    ##### https://www.loveandlemons.com/pesto-recipe/


### printing the response to see the text/info and also saying only 200 of it
print(response.text[:200])

###########################################

### using BeautifulSoup to scrape! or extract all the text and things from the websites and save them
response_soup_html = BeautifulSoup(response.text, "html.parser")

### this is actually getting the text...
response_soup_text = response_soup_html.get_text()


response_data = open('thisisnew.txt', 'w')
response_data.write(response_soup_text)
response_data.close
###### end of scraping code!!

### so start to markovify, open text and read it with .read
text = open("thisisnew.txt").read()

def getTitles(soupdata):
                            ### changing the header type
    titles = soupdata.select("h2")
    if titles:
        for t in titles:
            print(t.text)

print("\n\n\n")
print("this link has.......") 
getTitles(response_soup_html)   

###########################################

###### this is markovify!!!
### new method/function!! .Text needs an objective which is "text"
mushroom = markovify.Text(text)

paragraph = ""
### fun markovifying where it's making new paragraphs of words from text!
for x in range(10):
    paragraph += str(mushroom.make_short_sentence(100))
    paragraph += ""

print("\n\n\n")
print("here's a quick look:")
print("\n\n\n")
print(paragraph)
print("\n\n\n")

###########################################

#### a bit of code for finding the most common word! note tho i did copy this in from my unit2assignment1 but i tweaked it for this code algo here
file = open("thisisnew.txt" , "r")
### this is a dictionary 
word_counts = {}

for line in file:
    for word in line.split():
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        
        else:
            word_counts[word] = 1    

allPairs = iter((word_counts.items()))

Pair = next(allPairs)

mostFrequent1 = Pair[0]
for word in word_counts:
    if word_counts[word] > word_counts[mostFrequent1]:
        mostFrequent1 = word

print("fun fact! the first most common word here is:", mostFrequent1, "\nit appears", word_counts[mostFrequent1], "times!")

