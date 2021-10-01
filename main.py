import sys
import os
import random
from bs4 import BeautifulSoup
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from user_inputs import (
                    get_url,
                    get_user_choice,
                    get_slug,
                )
from file_handling import (
    create_project_directory,
    create_file,
)
from traversing import (
    randomly_traverse,
    utilitarianly_traverse   
)




def init_scraping():
    slug = get_slug()
    url = get_url(slug)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')
    # options.add_argument('blink-settings=imagesEnabled=false')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    driver.get(url)
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        print('')
    user_choice = get_user_choice()
    if user_choice == 1:
        print('Now the Random Traversing has begun')
        randomly_traverse(driver)
    else:
        utilitarianly_traverse(driver)




if __name__ == '__main__':
    init_scraping()