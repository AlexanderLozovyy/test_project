#!/usr/bin/python3
from bs4 import BeautifulSoup as BS
import requests as req

resp = req.get("http://192.168.122.66:5000/")

soup = BS(resp.text, 'html.parser')

for tag in soup.find_all('button'):
    print("{0} - {1}".format(tag.name, tag.text))