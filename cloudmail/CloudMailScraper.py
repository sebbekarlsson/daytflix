import requests
from requests import request, Request
import re
from bs4 import BeautifulSoup


class CloudMailScraper(object):

    def __init__(self):
        self.base_url = 'https://cloud.mail.ru/'
        self.session = requests.Session()

    def scrape_video_url(self, url):
        print(url)
        req = Request('GET', url, headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'})
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)

        soup = BeautifulSoup(response.text, 'html.parser')

        a = soup.find('a')

        print(a)
