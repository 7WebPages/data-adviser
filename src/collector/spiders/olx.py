from bs4 import BeautifulSoup
import requests

from ..base import BaseCollector


class OlxSpider(BaseCollector):
    """
    Olx.ua spider
    """

    name = 'OlxSpider'
    __CATEGORIES_ENTRYPOINT = 'http://olx.ua/sitemap/'
    __MAX_REQUESTS = 5

    def __init__(self):
        super(OlxSpider, self).__init__(self.__MAX_REQUESTS)

    def __repr__(self):
        return '<{0}>'.format(self.name)

    def run(self):
        pass

    def update_categories(self):
        response = requests.get(self.__CATEGORIES_ENTRYPOINT)
        soup = BeautifulSoup(response.text, self._PARSER)
        import pdb; pdb.set_trace()
        for s in soup.select('div.site-map').pop().find_all('a', class_='link'):
            print(s.attrs['href'], s.text)
