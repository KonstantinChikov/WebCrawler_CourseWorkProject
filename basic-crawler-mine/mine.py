import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import csv

def is_allowed_to_scrape(url):
    """
    Checks if scraping the given URL is allowed based on the site's robots.txt file.
    
    Args:
        url (str): The URL to check.
        
    Returns:
        bool: True if scraping is allowed, False otherwise.
    """
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch("*", url)
    except:
        print(f"Couldn't retrieve or parse robots.txt for {robots_url}. Proceeding with caution.")
        return False  # Default to False if there's an issue with robots.txt

def parse_site(url, html_tag, clazz):
    print(f'Checking if allowed to scrape {url}')
    if not is_allowed_to_scrape(url):
        print('Not allowed to scrape!')
        return
    
    print(f'Trying to crawl through {url}')
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print('Successfully retrieved the webpage\n')
        else:
            print('Failed to retrieve the webpage. Code: ', response.status_code)

    except ConnectionError as e:
        print('Connection Exception', e.args)
    except:
        print('General exception')

    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.title)
    print()

    print(f'All elements with css selector "{html_tag}.{clazz}"')
    elements = soup.find_all(html_tag, class_=clazz)
    for e in elements:
        print(e.get_text())
    
    # print(len(soup.select(f'{html_tag}.{clazz}')))
    print()

class SomeName:
    def __init__(self, site_url, html_tag, css_class) -> None:
        self.site_url = site_url
        self.html_tag = html_tag
        self.css_class = css_class


sites = [
    SomeName('https://www.scrapethissite.com/pages/', 'h3', 'page-title'),
    SomeName('https://crawler-test.com/', 'a', ''),
    SomeName('https://novini.bg/', 'h2', 'g-grid__item-title')
]

for site in sites:
    parse_site(site.site_url, site.html_tag, site.css_class)