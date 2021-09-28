from requests_html import HTMLSession
from bs4 import BeautifulSoup

def render_JS(URL):
    session = HTMLSession()
    r = session.get(URL)
    r.html.render(timeout=50)
    return r.html.raw_html



a = render_JS('https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2922')

soup = BeautifulSoup(a, 'html.parser')

print(soup.prettify())


