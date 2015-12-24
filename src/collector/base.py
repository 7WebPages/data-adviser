from abc import ABCMeta, abstractmethod
import asyncio


class BaseCollector(metaclass=ABCMeta):
    """
    Base class for all the spiders to inherit from
    """

    def __init__(self, max_requests):
        self.loop = asyncio.get_event_loop()
        self.sem = asyncio.Semaphore(max_requests)

    def __str__(self):
        return self.name

    @abstractmethod
    def update_categories(self):
        """
        Method that runs before main spider runs.
        It updates all the categories from source website
        """
