#import urllib, xml, ssl
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#prompt user for url run it through urllib, read the data and store it in variable"data" save xml into variable "xml"
#url = input("enter url here")
url = "https://py4e-data.dr-chuck.net/comments_1636703.xml"
data = urllib.request.urlopen(url).read()
xml = ET.fromstring(data.decode())

#create sum, add all xml comment/comments tags into a list "lst" run for loop to cycle through the tags and pull out the count text convert them to integers and add them to the sum

sum = 0
lst = xml.findall('comments/comment')
for item in lst:
    sum = sum + int(item.find('count').text)

print(sum)