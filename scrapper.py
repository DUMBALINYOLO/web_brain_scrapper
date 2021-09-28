import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')




driver.get("https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2751")


soup = BeautifulSoup(driver.page_source, 'html.parser')

zanda = []
for tag in soup.find_all('div', attrs={'class': 'thought'}):

    zanda.append(tag.text)


print(zanda)
    


