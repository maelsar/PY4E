import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#setting up input variables to be used in the loop
#url = input('Enter a url - ')
url = "https://py4e-data.dr-chuck.net/known_by_Lilias.html"
position = int(input('Enter list position - ')) - 1
num = int(input('Enter desired iterations - '))

#defining a function to call back to for each iteration
def parse(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    pos = 0
    for tag in tags:
        url = tag.get('href', None)
        pos = pos + 1
        if pos - 1 == position:
            return(url)

#iteration loop
iter = 0
while iter < num:
    parse(url, position)
    url = (parse(url, position))
    print(url)
    iter = iter + 1