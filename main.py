import sys
import os
import random
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from requests_html import HTMLSession





def create_project_directory(directory):
    if not os.path.exist(directory):
        print(f'Creating Directory {directory}')
        os.makedirs(directory)
    else:
        print(f'Directory with the name of {directory} already exits')




def create_file(node):
    queue = node + '-queue.txt'
    crawled = node + '-crawled.txt'
    if not os.path.isfile(crawled):
        write_file(crawled)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()








def get_slug():
    '''
    Unless their url slugs are deprecated then the following can get
    the slugs that important in loading the pages with the canvas and
    the first level subnodes

    Mystery Tours  >>  https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2762
    GateWays >> https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2750
    Declaration of Independence >> https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2922

    for now they are the only ones that matter till we choose otherwise


    '''
    print('Choose from the following options to proceed enjoy Drinking from the fountain of The Knowldge Web')
    print('>>Enter (1) to go Mystery Tours ')
    print('>>Enter (2) to go GateWays ')
    print('>>Enter (3) to go Declaration of Independence ')
    print('>>Enter (any key) to Exit ')

    try:
        slug = int(input('Enter your choice >>>  '))

        if slug == 1:
            return '#-2762'
        elif slug == 2:
            return '#-2750'
        elif slug == 3:
            return '#-2922'
        else:
            print('Try again')
            sys.exit()
    except ValueError:
        print('Sorry you need to put a number to proceed')
        sys.exit()



def get_url(slug):
    '''
        Concatanates slug to produce the url
    '''
    return  f'https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E{slug}'



def is_root_or_second_generation_node(text):
    '''
        The slugs/ids that are dynamically altered when you click on the node
        are hidden except in the source code and my assumption would be its 
        concealed in a react-router-dom like way of navigation. Therefore we are 
        left with no choice except for extracting all the text that lies in
        the divs with class thought ->
         <div 
            class="thought" 
            style="font-size: 15px; 
            top: 219px; 
            left: 217px; 
            color: rgb(255, 0, 0); 
            background-color: rgba(0, 0, 0, 0.5); 
            font-family: sans-serif; 
            padding: 2px; 
            opacity: 1; 
            z-index: 100;"
        >

        We extract the words and store them in a list and then filter out the root node
        and first generation nodes and we allow the user to choose from the filtered list
        which word would he/she want to follow in their scrapping adventure. The chosen
        word then is extracted and dynamically put into

            => driver.find_elements_by_xpath("//*[contains(text(), text)]")
                and then attempt to click the div
        This is so because the url links are changed when this div component is 
        clicked and then the tree node of the path is exposed when the div state
        is altered into active. It seems only one div with class thought can be
        active in the entire page, per an individual user query
   
    '''
    if text in ['The Knowledge Web', 'Gateways', 'Mystery Tours', 'Declaration of Independence']:
        return True
    else:
        return False


def get_user_choice(nodes):
    '''
        We try to make things interesting here by allowing the user to have an option:
            - purposively select a path leading to spawning children nodes of a node or
            - have a system randomly spawn a node for the user and proceed to the next step

        the we have a double level conditional algorithm > first to handle the above and secondly
        to make the user inputs is in the list of nodes 
    '''
    print('Choose either you would want the system to randomly choose a topic of interest or you want a determined outcome')
    print('Enter 1 for random >>>')
    print('Enter 2 for preffered topic >>>')

    node = int(input('Your choice >>  '))
    desired_choices = [1, 2]
    #we give three chances for the user to select the right choice in case their choice is not between 1/2
    if node in desired_choices:
        if node == desired_choices[0]:
            return random.choices(nodes)
        else:
            print('Choose one Topic from the List of Topics below')
            print(f'Your Topic Choices')
            for i, opt in enumerate(nodes):
                print(f'{i}: {opt}')
            node = input('Please type your choice as it is the list above here >>  ')
            if node in nodes:
                return node
            else:
                print('Make Sure You read the Instructions correctly and try again')
                #May need to have a while loop and give an end user multiple choices before
                #the program breaks
                sys.exit()
    else:
        print('Your choice is not in the list above. Follow the instructions and start the project again')
        #May need to have a while loop and give an end user multiple choices before
        #the program breaks
        sys.exit()
        

def filtered_nodes(text,nodes):
    # In scrapped texts that exist after clicking the div->thought ->active there
    # the root_or_second_generation_nodes are always avaliable. Hence a need to dump them
    # we also need to convert the list in a set to eliminate duplicates there are any
    deduplicated_nodes = set(nodes)
    filtered= []
    for node in deduplicated_nodes:
        #
        if is_root_or_second_generation_node(node) != True:
            filtered.append(node)
    return [node for node in filtered if node !=text]


def get_user_intention():
    print('Choose what you would want to do')
    print('Enter 1 if you intend to scrape and save only')
    print('Enter 2 if you intend to scrape, save and continue')
    print('Enter 3 if you intend to continue navigating through the tree nodes')
    #May need to have a while loop and give an end user multiple choices before
    #the program breaks if they selected a choice not in the list above
    user_intention = int(input('Please from the above and Enter your choice >>'))
    user_intention_params = [1, 2, 3]
    if user_intention in user_intention_params:
        if user_intention == 1:
            return 'Scrape & Save'
        elif user_intention == 2:
            return 'Scrape, Save & Continue'
        else:
            return 'Continue Navigating'       
    else:
        print('Sorry you failed to follow the Instructions')
        sys.exit()


def is_childless(nodes, text):
    '''
        When a node has no more childress its pointless to continue navigating
        You are only limited to the scrape only functionality and exit
    '''
    deduplicated_nodes = set(nodes)
    unpruned_nodes = []
    for node in deduplicated_nodes:
        if is_root_or_second_generation_node(node) != True:
            unpruned_nodes.append(node)
    children = [node for node in unpruned_nodes if node != text]
    if len(children) < 1: 
        return True
    else: 
        return False


def selenium_configuration():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    
    # driver.get(url)
    # # driver.implicitly_wait(50)

    # try:
    #     element = WebDriverWait(driver, 50).until(
    #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
    #     )
    # except:
    #     print('Is loading Fail')
    pass


def puppeteer_config():
    # r = session.get(url)
    # r.html.render(
    #     timeout=50,
    #     retries = 8, 
    #     script = None, 
    #     wait = 2.5, 
    #     scrolldown=True, 
    #     sleep = 10, 
    #     reload = True, 
    #     keep_page = True     
    # )
    # session = HTMLSession()

    pass


    



def init_scraping():
    slug = get_slug()
    url = get_url(slug)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    
    driver.get(url)
    # driver.implicitly_wait(50)

    try:
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        print('Is loading Fail')
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    nodes =[tag.text for tag in soup.find_all('div', attrs={'class': 'thought'}) if tag.text !='More Pins']
    
    # filtered_nodes(text,nodes)
    z = get_user_choice(nodes)
    print(z)





if __name__ == '__main__':
    init_scraping()
    


    