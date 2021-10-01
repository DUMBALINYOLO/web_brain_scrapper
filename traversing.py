import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from user_inputs import (
    get_user_intention,
    get_timer,
    get_user_choice,
)
from thought_generation import (
    get_listed_description
)


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



def get_traverse_choice(driver, user_choice):

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
        This is the Mecca of traversing over nodes in a utilitarian manner. You can
        dig deep as much as you want as long as the thought is childless
    
    '''
    choice = driver.find_element_by_xpath("//input[@class='searchBoxInput'][@type='text']")
    time.sleep(5)
    choice.send_keys(user_choice)
    time.sleep(5)
    element = driver.find_element_by_xpath('//li[contains(text(), "' + user_choice + '")]')
    time.sleep(5)
    driver.execute_script("arguments[0].click();", element)
    time.sleep(10)
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


def scrape_and_save(driver):
    print('Scrapping and Saving started ...')
    time.sleep(2)
    thought_detail = get_listed_description(driver)
    file=open('zero.txt','w')
    for items in  thought_detail:
        file.writelines(items+'\n')
    file.close()
    print('Scrapping Ended ...')


def scrape_save_and_continue(driver, nodes):
    print('Scrapping Saving & Continuing..')
    time.sleep(2)
    print('Continuing ...')
    continue_navigating(driver, nodes)


def continue_navigating(driver, nodes):
    print('The Navigation has just started ...')
    time.sleep(2)
    print('The Done ..')




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

    print('Choose one Topic from the List of Topics below')
    print('Your Topic Choices')
    for i, opt in enumerate(traverse_nodes):
        print(f'{i}: {opt}')
    try:
        node = int(input('Please Select your choices based on their numbers >>  '))
        if traverse_nodes[node] in traverse_nodes:
            # print(traverse_nodes[node])
            traverse_tree = get_traverse_choice(
                                    driver=driver, 
                                    user_choice=traverse_nodes[node]
                                )
            print(traverse_tree)
            user_intention = get_user_intention()
            if user_intention == 'Scrape & Save':
                scrape_and_save(driver=driver)
            elif user_intention == 'Scrape, Save & Continue':
                scrape_save_and_continue(driver=driver, nodes=traverse_tree)
            elif user_intention == 'Continue Navigating':
                continue_navigating(driver=driver, nodes=traverse_tree)
            else:
                user_intention = 'Quit'           
        else:
            print('Make Sure You read the Instructions correctly and try again')
            sys.exit()
    except ValueError:
        print('Sorry you need to put a number to proceed')
        sys.exit()