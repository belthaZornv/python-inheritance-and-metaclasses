class Metaclass(type):
    """
    Singleton metaclass used in AuthSession
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        print('Inside Metaclass.__init__')
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print('Inside Metaclass.__call__')
        return super().__call__(*args, **kwargs)

    def __new__(typ, *args, **kwargs):
        print('Inside Metaclass.__new__')
        return super().__new__(typ, *args, **kwargs)


class Parent:
    pass


class Internals(Parent, metaclass=Metaclass):
    def __init__(self):
        print('Inside Internals.__init__')
        pass

    def __call__(cls, *args, **kwargs):
        print('Inside Internals.__call__')
        pass


internals = Internals()
# invoke the __call__ method.
internals(a=5, b=5)

# Which dunder method gets called first?
# What are the arguments that are passed to the metaclass dunder methods?

# __new__ -> __init__ -> __call__ -> out of metaclass -> __init__
# Whats a metaclass? merely a callable, a class type, a type which alters the behavior of it's derived classes.

# cls - is the class implementing the type (Class Internals)
# name - class name (Internals)
# bases - base classes used (parent classes) (Parent Classes applied to Internals)
# attrs - are the attributes of the class implementing the type.
# all other attributes (namespace)
# __qualname__ - qualified name (PEP 3155) - doesn't include the module name

# __new__ method is passed the same attributes as the __init__ in the metaclass.

# Inside Metaclass.__new__
# Inside Metaclass.__init__
# Inside Metaclass.__call__
# Inside Internals.__init__
# Inside Internals.__call__
