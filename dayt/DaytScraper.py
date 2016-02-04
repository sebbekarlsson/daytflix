import requests
from requests import request, Request
import re
from bs4 import BeautifulSoup


class DaytScraper(object):

    def __init__(self):
        self.base_url = 'http://dayt.se/'
        self.query_url = '{}/forum/search.php'.format(self.base_url)
        self.session = requests.Session()

    def search(self, query, page, limit):
        req = Request('POST',  self.query_url,
                data={
                    'do': 'process',
                    'query': query,
                    'pp': limit,
                    'page': page
                    }
                )
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)

        searchid = self.scrape_searchid(response.text)

        req = Request('POST',  self.query_url,
                data={
                    'searchid': searchid,
                    'query': query,
                    'pp': limit,
                    'page': page
                    }
                )
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)

        video_urls = self.scrape_video_urls(response.text)
        videos = []

        for video_url in video_urls:
            videos.append({
                'title': video_url['title'],
                'url': video_url['url'],
                'mirrors': self.scrape_mirrors(video_url['url'])
            })

        
        return videos

    def scrape_searchid(self, html):
        return int(re.search('searchid=(().*)', html).group(1)\
                .replace('"', '').replace(';', ''))


    def scrape_video_urls(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        hrefs = soup.find_all('a', {'class': 'title'})
        video_urls = []

        for href in hrefs:
            video_urls.append({'title': href.text,'url': self.base_url+'/forum/'+ href['href']})

        return video_urls


    def scrape_mirrors(self, video_url):
        req = Request('GET', video_url)
        prepped = self.session.prepare_request(req)
        response = self.session.send(prepped)

        soup = BeautifulSoup(response.text, 'html.parser')

        mirror_1 = soup.find('a', id='dm1')['href']
        mirror_2 = soup.find('a', id='dm2')['href']
        mirror_3 = soup.find('a', id='dm3')['href']

        return mirror_1, mirror_2, mirror_3

