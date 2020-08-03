import requests
from bs4 import BeautifulSoup
import urllib.request

GOOGLE_IMAGE = 'https://www.google.com/search?tbm=isch&biw=1366&bih=606&q=' #main search string...Query to be added by main()
usr_agent = {
    # Used as header for the GET request
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'none',
    'Connection': 'keep-alive'
} 

def main():
    global GOOGLE_IMAGE
    imgString = input('Enter image to search for: ').split(' ')
    print('Searching...')
    # attaches query to search string
    for q in imgString:
        if GOOGLE_IMAGE[-1] == '=':
            search = q
        else:
            search = f'+{q}'
        GOOGLE_IMAGE += search

    response = requests.get(GOOGLE_IMAGE, headers=usr_agent)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = soup.find_all('div', attrs={"class": "isv-r"})

    for result in results:
        #Some results don't have a data-src attribute
        try:
            a = result.a.img['data-src'] # returns html link
        except KeyError:
            continue
        print(f'Image found: {a}')
        break

if __name__ == "__main__":
    main()
