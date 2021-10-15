from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())

url = "https://www.newegg.ca/samsung-1tb-980/p/N82E16820147804?Item=N82E16820147804&cm_sp=Dailydeal_SS-_-20-147-804-_-10152021"

result = requests.get(url)
doc2 = BeautifulSoup(result.text, "html.parser")

# print(doc2.prettify())

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong") # checks for the strong html tag
print(strong.string) # prints only the amount of price
