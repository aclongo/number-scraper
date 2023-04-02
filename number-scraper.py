# The program will use urllib to read the HTML from the data files below, 
# and parse the data, extracting numbers 
# and compute the sum of the numbers in the file.
    # Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_1768582.html 
        # (Sum ends with 45)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# You are to find all the <span> tags in the file 
# and pull out the numbers from the tag and sum the numbers.
# SAMPLE CODE: adjust this code to look for span tags 
# and pull out the text content of the span tag, 
# convert them to integers and add them up
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)