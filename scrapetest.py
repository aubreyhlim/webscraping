import ssl
import certifi
import urllib.request
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

# Create a SSL context object with certifi's certificates
context = ssl.create_default_context(cafile=certifi.where())

# Use the context to load the URL
try:
    html = urllib.request.urlopen('http://www.pythonscraping.com', context=context)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The serer could not be found")
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)