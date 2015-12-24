import aiohttp

from ..base import BaseCollector


class OlxSpider(BaseCollector):
    """
    Olx.ua spider
    """

    name = 'OlxSpider'
    __MAX_REQUESTS = 5

    def __init__(self):
        super(OlxSpider, self).__init__(self.__MAX_REQUESTS)

    def __repr__(self):
        return '<{0}>'.format(self.name)

    def run(self):
        pass

    def update_categories(self):
        print(self.loop)
