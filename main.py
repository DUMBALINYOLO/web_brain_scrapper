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
    We are handling exceptions  a lot when it comes to inputs to avoid a situation where 
    user inputs crush the code. We try by all means to give the end user 3 chances in every 
    mistake they commit so as to avoid the code just exiting after so much steps have been
    followed. 


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
            input_chances = 3
            while input_chances > 0:
                try:
                    slug = int(input('Enter your choice >>>  '))
                    input_chances -= 1
                    if slug == 1:
                        return '#-2762'
                        break
                    elif slug == 2:
                        return '#-2750'
                        break
                    elif slug == 2:
                        return '#-2922'
                        break
                except ValueError:
                    pass
            else:
                print('Sorry you need to follow instructions')
                sys.exit()
    except ValueError:
        input_chances = 3
        while input_chances > 0:
            try:
                slug = int(input('Enter your choice >>>  '))
                input_chances -= 1
                if slug == 1:
                    return '#-2762'
                    break
                elif slug == 2:
                    return '#-2750'
                    break
                elif slug == 2:
                    return '#-2922'
                    break
            except ValueError:
                print('Sorry you need to follow instructions')
                sys.exit()
        else:
            print('Sorry you need to follow instructions')
            sys.exit()



def get_url(slug):
    '''
        Concatanates slug to produce the url
    '''
    return  f'https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E{slug}'


def deduplicate_and_clean_root_nodes(nodes):
    '''
        In scrapped texts that exist after clicking the div->thought ->active there
        the root_or_second_generation_nodes are always avaliable. Hence a need to dump them
        we also need to convert the list in a set to eliminate duplicates there are any
        We are interested in dumping the root node (The Knowledge Web and its children)
    '''  
    deduplicated_nodes = set(nodes)
    filtered= []
    for node in deduplicated_nodes:
        #
        if is_root_or_second_generation_node(node) != True:
            filtered.append(node)
    return filtered



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
        Our exception handling is based on failure to borrow all the trust to our users when it
        comes to input. Where they are expected to put integers some can always go for strings
        thus strings can not be used as a param to index a list
        we give three chances for the user to select the right choice in case their 
        choice is not between 1/2

        for making a user friendly system we are allowing a user to choose
        the index value of a node hence the enumeration while looping over
        the nodes to show to a client
        hence all this cleaned_nodes[node] business
        yet to handle having three chances for every user input error as this is 
        the mother of the navigation process
    '''

    print('Choose either you would want the system to randomly choose a topic of interest or you want a determined outcome')
    print('Enter 1 for random >>>')
    print('Enter 2 for preffered topic >>>')

    cleaned_nodes = deduplicate_and_clean_root_nodes(nodes) 
    desired_choices = [1, 2]
    try:
        node = int(input('Your choice >>  '))

        if node in desired_choices:
            if node == desired_choices[0]:
                return random.choices(cleaned_nodes)[0]
            else:
                print('Choose one Topic from the List of Topics below')
                print(f'Your Topic Choices')
                for i, opt in enumerate(cleaned_nodes):
                    print(f'{i}: {opt}')
                try:
                    node = int(input('Please Select your choices based on their numbers >>  '))           
                    if cleaned_nodes[node] in cleaned_nodes:
                        return cleaned_nodes[node]
                    else:
                        print('Make Sure You read the Instructions correctly and try again')
                        sys.exit()
                except ValueError:
                    print('Sorry you need to put a number to proceed')
                    sys.exit() 
        else:
            print('Your choice is not in the list above. Follow the instructions and start the project again')
            sys.exit()
    except ValueError:
        print('Sorry you need to put a number to proceed')
        sys.exit()       



def filtered_nodes(text,nodes):
    '''
        We are concerned about filtering out the parent node from the list of children
    '''
    cleaned_nodes = deduplicate_and_clean_root_nodes(nodes)  
    return [node for node in cleaned_nodes  if node !=text]



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
    cleaned_nodes = deduplicate_and_clean_root_nodes(nodes) 
    children = [node for node in cleaned_nodes if node != text]
    if len(children) < 1: 
        return True
    else: 
        return False


def get_first_generation_grand_children(driver):

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    
    children =[tag.text for tag in soup.find_all('div', attrs={'class': 'thought'}) if tag.text !='More Pins']
    
    return children


def scrape_relations():
    pass




def init_scraping():
    slug = get_slug()
    url = get_url(slug)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')  
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        print('')
    children = get_first_generation_grand_children(driver)
    z = get_user_choice(children)
    print(z)





if __name__ == '__main__':
    init_scraping()
    


    