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
        # as opposed to interfaces abstract methods can
        # define an implementation
        return 'Hello World'


class BrokenImplementation(Abstract):
    pass


class WorkingImplementation(Abstract):
    def vanilla(self):
        # children classes, if so they wish can use the default
        # implementation of the baseclass
        
        text =  super().vanilla()
        return f'{text}!'

with TestCase().assertRaises(TypeError):
    BrokenImplementation()

assert WorkingImplementation().vanilla() == 'Hello World!'
