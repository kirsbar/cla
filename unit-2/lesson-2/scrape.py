# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

### requesting all the data and asking for all the html of the website
cla_response = requests.get("https://www.wikihow.com/Design-a-Small-Garden")
# phil_response = requests.get("https://www.newschool.edu/lang/philosophy/")

print(cla_response.text[:200])

cla_soup_html = BeautifulSoup(cla_response.text, "html.parser")
# phil_soup_html = BeautifulSoup(phil_response.text, "html.parser")

cla_soup_text = cla_soup_html.get_text()
# phil_soup_text = phil_soup_html.get_text()

cla_data = open('newfile.txt', 'w')
cla_data.write(cla_soup_text)
cla_data.close()

# phil_data = open('newschool-phil.txt', 'w')
# phil_data.write(phil_soup_text)
# phil_data.close()

### getting things in div brackets with this tag
def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.text)
      
print("CLA........")
getTitles(cla_soup_html)
# print("Philosophy.........")
# getTitles(phil_soup_html)

### use html to find certain information and match the tags to find it!