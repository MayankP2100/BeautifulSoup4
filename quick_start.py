from bs4 import BeautifulSoup
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoup method arranges the document nicely

# print(soup.prettify()) # to print the document formatted

print("1 ", soup.title)               # prints the title tag
print("2 ", soup.title.name)          # prints title as a name
print("3 ", soup.title.string)        # prints the title as a string
print("4 ", soup.title.parent.name)   # prints the title's parent tag
print("5 ", soup.p)                   # first <p/> tag in the document
print("6 ", soup.p["class"])          # first class'name inside the first p tag
print("7 ", soup.a)                   # prints first <a/> tag
print("8 ", soup.find_all("a"))       # finds all the <a/> tags
print("9 ", soup.find(id="link3"))    # finds  the given id by string name

print()

for link in soup.find_all('a'):
    print("10 ", link.get('href'))  # prints all the href var in all of the <a/> tags

print()

print("11 ", soup.get_text())   # gets all of the text in the document
