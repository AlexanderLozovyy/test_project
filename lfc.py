#!/usr/bin/python3
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://192.168.122.66:5000/')

def getcolor(elementid):
    element = driver.find_element_by_id(elementid)
    return element.value_of_css_property('background-color')

button1 = 'a'
button2 = 'b'

buttons = [button1, button2]

for button in buttons:
    print(button, ' - ', getcolor(button))