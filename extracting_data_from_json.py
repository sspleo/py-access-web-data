import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1:
        break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    comments = info["comments"]

    tot = 0
    for comment in comments:
        tot = tot + int(comment["count"])
    print('Count:', len(comments))
    print('Sum:', tot)
