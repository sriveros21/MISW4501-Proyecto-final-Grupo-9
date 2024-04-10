from abc import ABC, abstractmethod

class BaseQuery(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")