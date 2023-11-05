from bs4 import BeautifulSoap


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoap(contents, "html.parser")
print(soup.title)
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
