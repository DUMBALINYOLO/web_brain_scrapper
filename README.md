# web_brain_scrapper
Scrapping Web Brain using python

This code is still 3/4 away from being finished.
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
