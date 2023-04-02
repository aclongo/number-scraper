# ASSIGNMENT: extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find
    # Start at: http://py4e-data.dr-chuck.net/known_by_Banan.html
    # Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
    # Hint: The first character of the name of the last page that you will load is: Z

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
position = int(input('Enter position: '))
count = int(input('Enter count: '))
print('Retrieving:', url)

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst = []
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        lst.append(tag.get('href', None))
    url = lst[position - 1]
    print('Retrieving:', url)
    count -= 1