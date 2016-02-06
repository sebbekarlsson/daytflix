import requests
from requests import request, Request
import re
from bs4 import BeautifulSoup


class CloudMailScraper(object):

    def __init__(self):
        self.base_url = 'https://cloud.mail.ru/'
        self.session = requests.Session()
        self.base_view_url = 'https://cloclo116.datacloudmail.ru/weblink/view/'
        self.url_args = '?etag=BD364531B0D85B8DD1A9A951608F3C0CCD6F4DB1&key=ba331653c4f0fdaf7b38ad4b76954f9b0b6e1990'

    def scrape_video_url(self, url):
        url = url.replace('https://cloud.mail.ru/public/', self.base_view_url) + self.url_args
        print(url)
        req = Request('GET',
                url,
                headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36', 'Content-Type': 'video/mp4'}
        )
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)

        print(response)

        #soup = BeautifulSoup(response.text, 'html.parser')

        #print(a)
