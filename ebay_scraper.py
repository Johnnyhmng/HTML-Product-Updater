from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#Gets html from url and makes BS4 object
url       = 'https://vi.vipr.ebaydesc.com/ws/eBayISAPI.dll?ViewItemDescV4&item=292762557824&t=1539612313000&tid=10&category=170098&seller=canopystreet&excSoj=1&excTrk=1&lsite=0&ittenable=false&domain=ebay.com&descgauge=1&cspheader=1&oneClk=1&secureDesc=1'
uClient   = urlopen(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

############################################################################################################

#Gets title of product
title = page_soup.find("div", {"class", 'description'})

#Meta Tags
meta_title = page_soup.find("meta", {"name": "title"})
meta_description = page_soup.find("meta", {"name": "description"})
title_description = title.find('h2') 

#Gets li 
li_description = title.find('ul')

#Replaces meta tags and description
meta_title.replace_with(r'<meta name="title" content={0}>')
meta_description.replace_with(r'<meta name="description" content={1}>')
title_description.replace_with(r'<h2>{2}</h2>')

#Replaces li descriptions
#li_description.replace_with(r'')


finished_html = str(page_soup)

finished_html = finished_html.replace(r"&lt;", r"<")
finished_html = finished_html.replace(r"&gt;", r">")

#Create a file and open it up for writing
with open('RevisedHtml.html', 'w') as html_file:
    #Write html to file
    html_file.write(finished_html)
