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
# and pull out the text content of the span tag, 
# convert them to integers and add them up
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>

# Initialize a sum total variable
sum = 0
span_tags = soup('span')
for tag in span_tags:
    # Pull out contents of span tag
    print('TAG:', tag)
    # Save the text content of each span tag in a variable
    content = tag.contents[0]
    print('NUMBER OF COMMENTS:', content)
    # Convert the text content to an integer and add to the total
    sum += int(content)
    print('RUNNING TOTAL:', sum)

print(f'\nFINAL: There were a total of {sum} comments on the webpage url {url}.')