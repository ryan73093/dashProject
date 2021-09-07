from abc import ABC
from abc import abstractmethod


class Step(ABC):
    # 子孫的class不打算撰寫init，因此不加abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass