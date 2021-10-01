
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





def get_user_choice():
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





def get_user_intention():
    print('Choose what you would want to do')
    print('Enter 1 if you intend to scrape and save only')
    print('Enter 2 if you intend to scrape, save and continue')
    print('Enter 3 if you intend to continue navigating through the tree nodes')
    print('Enter 4 if you want to stop')
    #May need to have a while loop and give an end user multiple choices before
    #the program breaks if they selected a choice not in the list above
    user_intention_params = [1, 2, 3, 4]
    try:
        user_intention = int(input('Please from the above and Enter your choice >>  '))    
        if user_intention in user_intention_params:
            if user_intention == 1:
                return 'Scrape & Save'
            elif user_intention == 2:
                return 'Scrape, Save & Continue'
            elif user_intention == 3:
                return 'Continue Navigating'
            else:
                return 'Quit'
        else:
            print('Please follow these instructions')
            print('Enter 1 if you intend to scrape and save only')
            print('Enter 2 if you intend to scrape, save and continue')
            print('Enter 3 if you intend to continue navigating through the tree nodes')
            print('Enter 4 if you want to stop')
            input_chances = 3
            while input_chances > 0:
                try:
                    intention = int(input('Enter your choice >>>  '))
                    input_chances -= 1
                    if intention == 1:
                        return 'Scrape & Save'
                        break
                    elif intention == 2:
                        return 'Scrape, Save & Continue'
                        break
                    elif intention == 3:
                        return 'Continue Navigating'
                        break
                    else:
                        return 'Quit'
                except ValueError:
                    print('Please follow these instructions')
                    print('Enter 1 if you intend to scrape and save only')
                    print('Enter 2 if you intend to scrape, save and continue')
                    print('Enter 3 if you intend to continue navigating through the tree nodes')
                    print('Enter 4 if you want to stop')
                    intention = int(input('Enter your choice >>>  '))
                    input_chances -= 1
                    if intention == 1:
                        return 'Scrape & Save'
                        break
                    elif intention == 2:
                        return 'Scrape, Save & Continue'
                        break
                    elif intention == 3:
                        return 'Continue Navigating'
                        break
                    else:
                        return 'Quit'
            else:
                print('Sorry you need to follow instructions')
                sys.exit()
    except ValueError:
        print('Please follow these instructions')
        print('Enter 1 if you intend to scrape and save only')
        print('Enter 2 if you intend to scrape, save and continue')
        print('Enter 3 if you intend to continue navigating through the tree nodes')
        print('Enter 4 if you want to stop')
        input_chances = 3
        while input_chances > 0:
            try:
                intention = int(input('Enter your choice >>>  '))
                input_chances -= 1
                if intention == 1:
                    return 'Scrape & Save'
                    break
                elif intention == 2:
                    return 'Scrape, Save & Continue'
                    break
                elif intention == 3:
                    return 'Continue Navigating'
                    break
                else:
                    return 'Quit'
            except ValueError:
                print('Please follow these instructions')
                print('Enter 1 if you intend to scrape and save only')
                print('Enter 2 if you intend to scrape, save and continue')
                print('Enter 3 if you intend to continue navigating through the tree nodes')
                print('Enter 4 if you want to stop')
                intention = int(input('Enter your choice >>>  '))
                input_chances -= 1
                if intention == 1:
                    return 'Scrape & Save'
                    break
                elif intention == 2:
                    return 'Scrape, Save & Continue'
                    break
                elif intention == 3:
                    return 'Continue Navigating'
                    break
                else:
                    return 'Quit'
        else:
            print('Sorry you need to follow instructions')
            sys.exit()




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

