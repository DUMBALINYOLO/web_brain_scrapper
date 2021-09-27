import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
#
response = requests.get('https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2762')
content = response.content
soup = BeautifulSoup(content, 'html.parser')
#
#
#
#
# def get_junk(soup):
#     junk = []
#     for tag in soup.find_all('span', attrs={'class': 'menuText'}):
#         junk.append(tag.text)
#     return junk
#
# zendia = []
# for tag in soup.find_all('div'):
#     zendia.append(tag)
#
# print(soup.prettify())
# driver.get("https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2751")
# elem = driver.find_element_by_id('contentContainer')
#
# print(elem.source)

thingings = []
for tag in soup.find_all('div', attrs={'id': 'contentContainer'}):
    thingings.append(tag)

print(thingings)
