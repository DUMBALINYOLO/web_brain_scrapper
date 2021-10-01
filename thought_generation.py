

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


def get_thought_body(driver):
    '''
       so much to be gotten here by proxy functions to keep the code a little bit clean

       Some of the function calls can return None,
       For all those that return None shall be filtered out of the dict
       
       There seem to be some conditional rendering on the site whereby some components
       are meant to display user profiles, some quotations and some a deep description
       of a certain topic. Its only when the return value is None that we we do away with
       the thinging
    '''


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
    



def get_proffessional_links(driver):
    '''
        This applies especially to individuals. Digging deeper we shall try to handle exceptions
        where these are not found

        reference
        <div class="GGD0W3FBH4">http://kwebarchive.com/william-archer/</div>
    '''
    # proffesional_link = soup.find_all('div', attrs={'class': 'GGD0W3FBH4'})

    pass


def get_source_links(driver):
    '''
    
    '''



def get_profile_details(driver):

    '''
        <div class="gwt-HTML" aria-hidden="false">
    '''
    # image = 

    pass

def get_image(driver):
    # image = soup.find('div', attrs={'class': 'gwt-HTML'})
    # locate a picture
    pass

def get_description(driver):
    pass



def get_link(driver):
    '''
        find a tag and get href
    '''

    # soup.find('div', attrs={'class': 'gwt-HTML'})
    pass


def get_listed_description(driver):
    '''
        Some Descriptions seem to be stored in <div class='gwt-HTML'>
                                                    <p class='MsoNormal'>
                                                        <b>....</b>
                                                    </p>
                                                </div>
        gwt-HTML.MsoNormal.
    '''
    description = [tag.text for tag in driver.find_elements_by_class_name('MsoNormal')]

    return description



def get_bibliography(driver):
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


def get_images(driver):
    '''
        image = soup.find('div', attrs={'class': 'gwt-HTML'})
        locate pictures in descriptions

        <p class="MsoNormal" style=" text-autospace: none;">
            <img src="">
        </p>

    '''
   
    pass
