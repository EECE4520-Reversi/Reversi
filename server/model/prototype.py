from abc import ABC, abstractmethod


class Prototype(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def clone():
        pass
