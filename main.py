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







def create_project_directory(directory):
    '''
     shall create folders based on datatetime.date
    '''
    
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
    STEPS:
        This is the most important important step in scrapping this site as it sets the
        path by which the end user would want to traverse the site and start the etl 
        proccess.
        Mystery Tours  >>  https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2762
        GateWays >> https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2750
        Declaration of Independence >> https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2922
        
    LOGIC:
        This site is set up in two methodologies for spawning the nodes and read through
        data.
            (1) -- The User can Choose in the tree which direction to take by clicking
                on top of thoughts read over them or continue spawning its nodes
            (2) -- Right Click on the Canvas and Select the clickLink Wander and then
                the side will go on to pseudo-randomly traversy through the trees, read
                and then proceed walking through different toughts
        There was a realization that when the site is at The Knowledge Web URL if Wander
        is selected it pseudo-randomly selects from its children and stops there. Hence
        a need to elevate the traversing to start from the first generation children
    
    EXCEPTION HANDLING:
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





def get_user_choice() -> int:
    '''
        We try to make things interesting here by allowing the user to have an option:
            - purposively select a path leading to spawning children nodes of a node or
            - have a system randomly spawn a node from traversing the trees using a clickMenu 
            - Link with text Wander

        the we have a double level conditional algorithm > first to handle the above and secondly
        to make the user inputs is in the list of nodes
        Our exception handling is based on failure to borrow all the trust to our users when it
        comes to input. Where they are expected to put integers some can always go for strings
        we give three chances for the user to select the right choice in case their
        choice is not between 1/2     
    '''

    print('Choose either you would want the system to randomly choose a topic of interest or you want a determined outcome')
    print('Enter 1 for random >>>')
    print('Enter 2 for preffered topic >>>')

    
    desired_choices = [1, 2]
    try:
        choice= int(input('Your choice >>  '))
        if choice in desired_choices:
            return choice             
        else:
            choices_chances = 3
            while choices_chances > 0:
                try:
                    choice = int(input('Enter your choice >>>  '))
                    choices_chances -= 1
                    if choice in desired_choices:
                        return choice
                        break  
                except ValueError:
                    print('Please try to use an Integer to proceed')
                    choice = int(input('Enter your choice >>>  '))
                    choices_chances -= 1
                    if choice in desired_choices:
                        return choice
                        break
            else:
                print('Sorry you have failed to understand the instructions. Try again')
                sys.exit()     

    except ValueError:
        choices_chances = 3
        while choices_chances > 0:
            try:
                choice = int(input('Enter your choice >>>  '))
                choices_chances -= 1
                if choice in choice in desired_choices:
                    return choice    
            except ValueError:
                print('Please try to use an Integer to proceed')
                choice = int(input('Enter your choice >>>  '))
                choices_chances -= 1
                if choice in desired_choices:
                    return choice
                    break
        else:
            print('Sorry you have failed to understand the instructions. Try again')
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
                and then attempt to click the div ... I may have taken the hard path here
            => well there seem to be a better way and it has to do with the searchBox and ul.stationaryClickMenu li
            => we need to manipulate these guys in order to start playing around and scrapping
        This is so because the url links are changed when this div component is
        clicked and then the tree node of the path is exposed when the div state
        is altered into active. It seems only one div with class thought can be
        active in the entire page, per an individual user query


    '''
    if text in [
            'The Knowledge Web', 
            'Gateways', 
            'Mystery Tours', 
            'Declaration of Independence',
            '',
        ]:
        return True
    else:
        return False




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



def get_first_generation_grand_children(driver):

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # we are  going to be deprecating this king of text extraction as the overflow is hidden for long nodes and we wouldn't
    # want to extract an unfinshed node with a ...
    children =[tag.text for tag in soup.find_all('div', attrs={'class': 'thought'}) if tag.text !='More Pins']

    return children



def get_timer():
    '''
        probing the end user for the minutes which he/she would want the program to run in a random
        mode
    '''
    
    
    print('Please Select the minutes which you would want your program to run for')
    try:
        minutes_to_run = int(input('Insert number of minutes greater than 0'))
        if minutes_to_run >= 1:
            current_time = int(time.time())
            time_now = int(time.time())
            if time_now >= current_time + (minutes_to_run * 60):
                return True
            else:
                return False
        else:
            chances = 3
            while chances > 0:
                try:   
                    minutes_to_run = int(input('Insert number of minutes greater than 0'))
                    if minutes_to_run >= 1:
                        current_time = int(time.time())
                        time_now = int(time.time())
                        if time_now >= current_time + (minutes_to_run * 60):
                            return True
                            break
                        else:
                            return False
                            break
                except ValueError:
                    print('Please Start Again and try to input a number')
            else:
                print('Sorry you have exhausted your chances. Try by all means to follow instructions')
    except ValueError:
        print('You need to follow instructions')
        chances = 3
        while chances > 0:
            try:   
                minutes_to_run = int(input('Insert number of minutes greater than 0'))
                if minutes_to_run >= 1:
                    current_time = int(time.time())
                    time_now = int(time.time())
                    if time_now >= current_time + (minutes_to_run * 60):
                        return True
                        break
                    else:
                        return False
                        break
            except ValueError:
                print('Please Start Again and try to input a number')
                sys.exit()
        else:
            print('Sorry you have exhausted your chances. Try by all means to follow instructions')
            sys.exit()



def make_new_thought():
    '''
        We will first return a python dict then clean it into a .txt file
    '''
    return {
        'get_proffessional_links' : None,
        'get_source_links': None,
        'get_profile_details': None,
        'get_image': None,
        'get_description': None,
        'get_link': None,
        'get_listed_description': None,
        'get_images': None,
        'get_bibliography': None,
        
    }


def get_thought_body(page_source):
    '''
       so much to be gotten here by proxy functions to keep the code a little bit clean

       Some of the function calls can return None,
       For all those that return None shall be filtered out of the dict
       
       There seem to be some conditional rendering on the site whereby some components
       are meant to display user profiles, some quotations and some a deep description
       of a certain topic. Its only when the return value is None that we we do away with
       the thinging
    '''

    soup = BeautifulSoup(page_source, 'html.parser')
    methods = [
        get_proffessional_links,
        get_source_links,
        get_profile_details,
        get_image,
        get_description,
        get_link, 
        get_listed_description,
        get_images,
        get_bibliography,

    ]

    thought = make_new_thought()

    thought = thought

    for method in methods:
        try:
            partial_thought = method(soup)
            if partial_thought is None:
                print("Extract method %s didn't return anything", method.__name__)
                continue
            thought.update(partial_thought)
        except Exception as ex:
            print("")
    return thought
    



def get_proffessional_links(soup):
    '''
        This applies especially to individuals. Digging deeper we shall try to handle exceptions
        where these are not found

        reference
        <div class="GGD0W3FBH4">http://kwebarchive.com/william-archer/</div>
    '''
    proffesional_link = soup.find_all('div', attrs={'class': 'GGD0W3FBH4'})

    return proffesional_link


def get_source_links(soup):
    '''
    
    '''



def get_profile_details(soup):

    '''
        <div class="gwt-HTML" aria-hidden="false">
    '''
    # image = 


    parent_div = soup.find('div', attrs={'class': 'gwt-HTML'})
    pass

def get_image(soup):
    # image = soup.find('div', attrs={'class': 'gwt-HTML'})
    # locate a picture
    pass

def get_description(soup):
    description = soup.find('div', attrs={'class': 'gwt-HTML'}).text

    return description



def get_link(soup):
    '''
        find a tag and get href
    '''

    # soup.find('div', attrs={'class': 'gwt-HTML'})
    pass


def get_listed_description(soup):
    '''
        Some Descriptions seem to be stored in <div class='gwt-HTML'>
                                                    <p class='MsoNormal'>
                                                        <b>....</b>
                                                    </p>
                                                </div>
        gwt-HTML.MsoNormal.
    '''
    pass


def get_bibliography(soup):
    '''
        <div class='gwt-HTML'>
            <ul>
                <li class='MsoNormal'>
                    <b>
                        text 
                        <i>....</>
                    
                    </b>
                </li>
            
            </ul>
            
        </div>
    

    '''
    pass


def get_images(soup):
    '''
        image = soup.find('div', attrs={'class': 'gwt-HTML'})
        locate pictures in descriptions

        <p class="MsoNormal" style=" text-autospace: none;">
            <img src="">
        </p>

    '''
   
    pass




def randomly_traverse(driver):

    '''
        PATH == 1
            IF USER CHOOSES TO GO WITH THE RANDOM CHOICE THEN HE/SHE WILL BE LED TO THIS PATH
        
        UNCERTAINITY:
            NOT YET SURE IF THE TREES ARE TRAVERSED THROUGH A LINEAR RELATION WHERE BY IT SPAWNS
            LINKS BASED ON MOTHER CHILD RELATION GOING INTO GENERATIONS OF CHILDREN OR IT JUST
            WALKS OVER PARENTS CHILDREN SIBBLINGS BACK AND FOURTH

        INTENTION:
            WE TARGET TO CLICK ON THE WANDER LINK AND CONTINUE TRAVERSING. I DONT IF IT SHALL BE
            NECCESSARY BUT WE SHALL TRY TO SET A TIME INTERVAL INTERVAL BY WHICH THE PROGRAM SHOULD
            RUN AND THEN TERMINATE AFTERWARDS TO AVOID THE PROGRAM RUNNING FOR EVER

        THIS IS WHERE ALL EVERYTHING THAT HAS TO DO WITH RANDOM SCRAPPING HAPPENS
        <li class="clickItem">Wander</li>
    '''
    while True:
        element = driver.find_element_by_xpath('//li[contains(text(), "' + 'Wander' + '")]')
        driver.execute_script("arguments[0].click();", element)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "myDynamicElement"))
            )
        except:
            print('')
    else:
        print('Your time for randomly scrapping over Web Brain Website has lapsed')


def is_childless(nodes, text):
    '''
        When a node has no more childress its pointless to continue navigating
        You are only limited to the scrape only functionality and exit
    '''
    cleaned_nodes = deduplicate_and_clean_root_nodes(nodes)

    children = [
            node for node \
            in cleaned_nodes 
            if node != text
        ]
        

    if len(children) < 1:
        return True
    else:
        return False


def tree_traverse(old_nodes,  new_nodes):
    '''
        The utilitarian traversing is quite complex and each tree spawns new nodes.
        However there is always a situation where the old list is not cleared in
        the page source. This function filters out all old nodes from the new nodes.
        This function allows one to go on traversing as they deem necesseary its stopped
        by its helper function is childless
        
    '''

    return [
            node for node\
            in new_nodes if node\
            not in old_nodes
        ]



def get_traverse_choice(driver):

    '''
        <
            input 
            type="text" 
            class="searchBoxInput" 
            style="white-space: nowrap; height: 20px;"
        >
        <li 
            class="clickItem"
        >
            Bananas to Logarithms
        </li>
    
    '''
    choice = driver.find_element_by_xpath("//input[@class='searchBoxInput'][@type='text']")
    time.sleep(3)
    choice.send_keys('Barometer')
    time.sleep(3)
    element = driver.find_element_by_xpath('//li[contains(text(), "' + 'Barometer' + '")]')
    time.sleep(3)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    thoughts = [tag.text for tag in driver.find_elements_by_class_name('thought')]
    cleaned_nodes = deduplicate_and_clean_root_nodes(thoughts)
    return cleaned_nodes



def get_first_generation_node_children(driver):
    '''
        We are concerned about filtering out the parent node 
        from the list of children. 
    '''
    time.sleep(2)
    thoughts = [tag.text for tag in driver.find_elements_by_class_name('thought')]
    cleaned_nodes = deduplicate_and_clean_root_nodes(thoughts)

    return cleaned_nodes


    

def utilitarianly_traverse(driver):
    '''
        for making a user friendly system we are allowing a user to choose
        the index value of a node hence the enumeration while looping over
        the nodes to show to a client
        hence all this cleaned_nodes[node] business
        yet to handle having three chances for every user input error as this is
        the mother of the navigation process
    '''
    traverse_nodes = get_first_generation_node_children(driver)
    print(traverse_nodes)

    # nodes = get_traverse_choice(driver)
    # print(nodes)

    # print('Choose one Topic from the List of Topics below')
    # print(f'Your Topic Choices')
    # for i, opt in enumerate(nodes):
    #     print(f'{i}: {opt}')
    # try:
    #     node = int(input('Please Select your choices based on their numbers >>  '))
    #     if nodes[node] in nodes:
    #         return nodes[node]
    #     else:
    #         print('Make Sure You read the Instructions correctly and try again')
    #         sys.exit()
    # except ValueError:
    #     print('Sorry you need to put a number to proceed')
    #     sys.exit()



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
