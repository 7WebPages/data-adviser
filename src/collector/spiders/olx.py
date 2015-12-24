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
        page = requests.get(self.__CATEGORIES_ENTRYPOINT)
        print(page)
