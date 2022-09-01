import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#prompt user for url run it through urllib, read the data and store it in variable"data" save xml into variable "xml"
#url = input("enter url here")
url = "https://py4e-data.dr-chuck.net/comments_1636704.json"
data = urllib.request.urlopen(url).read()

info = json.loads(data)
print('User count:', len(info))

datalist = info['comments']
#print(datalist)

ttl = 0

for item in datalist:
    ttl = ttl + int(item['count'])
    #print(item['count'])

print(ttl)
