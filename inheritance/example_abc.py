from abc import ABCMeta, abstractmethod
from unittest import TestCase

# class Abstract(ABC): is equivelent to using the metaclass


class Abstract(metaclass=ABCMeta):
    @abstractmethod
    def vanilla(self):
        """
        Hello there
        :return:
        """


class Implementation(Abstract):
    pass


with TestCase().assertRaises(TypeError):
    Implementation()
