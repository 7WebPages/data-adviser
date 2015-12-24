from .spiders import *


class SpiderRunner(object):
    """
    Class to run all the spiders
    """

    __spiders = []

    def __init__(self, providers):
        for provider in providers:
            cls_name = provider.name + 'Spider'
            if cls_name in globals():
                self.__spiders.append(globals()[cls_name])

    def run(self):
        for spider in self.__spiders:
            spider_instance = spider()
            spider_instance.run()

    def update_categories(self):
        for spider in self.__spiders:
            spider_instance = spider()
            spider_instance.update_categories()
