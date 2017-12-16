import urllib
import os
import requests
from bs4 import BeautifulSoup

source = requests.get('https://history.nasa.gov/shuttle_patches.html')
soup = BeautifulSoup(source.text, 'html.parser')

for link in soup.find('li').find_all('a'):
    image_link = (link.get('href'))
    image = requests.get(image_link)
    name = image_link[40:-4]
    with open(name + '.jpg', "wb") as f:
        f.write(image.content)







