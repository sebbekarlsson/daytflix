from dayt.DaytScraper import DaytScraper
from cloudmail.CloudMailScraper import CloudMailScraper


class DaytFlix(object):

    def __init__(self):
        self.daytScraper = DaytScraper()
        self.cloudmailScraper = CloudMailScraper()


    def search(self, query, page, limit):
        videos = self.daytScraper.search(query, page, limit)

        for video in videos:
            uuu  = self.cloudmailScraper.scrape_video_url(video['mirrors'][2])
            
