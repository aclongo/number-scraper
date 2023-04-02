# ASSIGNMENT: extract the href values from the anchor tags, 
# scan for a tag that is in a particular position relative to the first link in the list, follow that link and repeat the process a number of times

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for a starting url
url = input('Enter URL: ')
# Ask what link position relative to the first link will be followed
position = int(input('Enter position: '))
# Ask how many links will be followed, including the starting url
count = int(input('Enter count: ')) + 1

# Execute this block for each link followed until the counter runs down
while count > 0:
    print('Retrieving:', url) # Print current url being parsed
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst = [] # Create an empty list for the anchor tag links
    tags = soup('a') # Retrieve all of the anchor tags
    for tag in tags:
        # Append each url found in the tags to the empty list
        lst.append(tag.get('href', None))
    # Index the url indicated by position, factoring in that indexes actually begin at 0
    url = lst[position - 1]
    # Decrement the counter
    count -= 1