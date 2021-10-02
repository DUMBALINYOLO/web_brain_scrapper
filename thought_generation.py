

def make_new_thought():
    '''
        We will first return a python dict then clean it into a .txt file
    '''
    return {
        # 'get_proffessional_links' : None,
        'get_source_links': None,
        # 'get_profile_details': None,
        # 'get_image': None,
        'get_description_one': None,
        'get_description_two': None,
        # 'get_listed_description': None,
        # 'get_images': None,
        # 'get_bibliography': None,
        
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
        get_source_links(driver),
        get_description_one(driver),
        get_description_two(driver),

    ]

    return methods




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
    links = [link.get_attribute("href") for link in driver.find_elements_by_css_selector(".gwt-HTML a")]
    return links




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


def get_description_one(driver):
    '''
        Some Descriptions seem to be stored in <div class='gwt-HTML'>
                                                    <p class='MsoNormal'>
                                                        <b>....</b>
                                                    </p>
                                                </div>
        gwt-HTML.MsoNormal.
    '''
    # description = [tag.text for tag in driver.find_elements_by_class_name('MsoNormal')]
    # if description is not None:
    #     return description
    # else:
    # description = [tag.text for tag in driver.find_elements_by_class_name('gwt-HTML')]
    description = [tag.text for tag in driver.find_elements_by_css_selector(".gwt-HTML p")]

    return description



def get_description_two(driver):
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
   
    images = [src.get_attribute("src") for src in driver.find_elements_by_css_selector(".gwt-HTML img")]
    return images