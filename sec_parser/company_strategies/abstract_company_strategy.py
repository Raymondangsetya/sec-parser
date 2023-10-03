from abc import ABC, abstractmethod

class CompanyStrategy(ABC):
    @abstractmethod
    def process(self, element):
        pass
