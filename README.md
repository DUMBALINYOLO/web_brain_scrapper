# web_brain_scrapper
Scrapping Web Brain using python

This code is still 1/3 away from being finished.
Still more to come as the next steps have to do with livening up the selenium robotic process
and at least try to mess with manipulating those tree nodes and then write the scrapped data
to the files. requests-html was tested in the curiosity of the selenium versus puppeteer debacle
but I would rather go with selenium, for as long as it can wait for javascript to load in the
browser then we are cool. This is just a test project and int a production ready projects
we would rely more on the Argpase module to make our inputs more fun and swift.
But for now we are just using raw python just to see how best can we use simple logic to navigate
into all pages for fun.


The css files are just for understanding some elements and try locate some elements through their css
paths in order to call actions like this

elements = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "img.market_listing_item_img.economy_item_hoverable")))



(1) have figured out everything. Now I am left with hovering over the css hidden components
(2) make the the the user choice inputs iterate based on the desired actions
(3) I am two days away from wrapping up
(4) The project has been split into files so as to avoid the main file being too big to
    write
(5) The is a need to do so much parsing of different text containers as the site is not
    consisted on how the thought details are stored, we will have to handle returning none on some of them and capture those which matter. So we shall sample more than 20 different
    scenarios and handle them in a manner where there are small chances of the program
    hitting a brickwall
(6) The program has started scrapping and saving. Now we go on and handle navigation, scrapping
    saving
(7) Number 5 shall be deeply should there be an agreed way how the data can be presented and     since it demands time. At least to go deep there shall be a principal agreement if I should continue and go deeper int the project or what

(8) After tomorrow there shall be more posibilities on many improvements that can be done on the
    project and take to a level where its quite amazing

(9) The subfolders belong to the scrapped first_generation_grand_children

(10) Those with an empty .txt file is an indication that information is stored in different
      boxes and we should go deeper and at least figure out all these mysterious boxes

(11) Some of these links are just empty as thoughts and they are just there to lead one to somewhere

(12) Python Dictionaries are going to come in hand as I would want to utilise a breadth-first-search (the loop/non-recursive version) to create an autopilot scrapper that keep relations
