# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))

exc = 0
while exc <= cnt:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags <a ... > to <\a>
    tags = soup('a')
    if exc == 0:
        print('Retrieving:', url)
    else:
        tag = tags[pos - 1].get('href', None)
        print('Retrieving:', tag)
        url = tag
    exc += 1
