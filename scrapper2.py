from requests_html import HTMLSession

def render_JS(URL):
    session = HTMLSession()
    r = session.get(URL)
    r.html.render(timeout=50)
    return r.html.find('.thought', first=True),





a = render_JS('https://webbrain.com/brainpage/brain/C6015FA0-82BF-F1FA-9D05-0EA9FD7F845E#-2762')

print(a.html)
