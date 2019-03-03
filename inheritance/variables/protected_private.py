class Perm:
    _abc = 1
    """ 
    Protected attribute - author doesn't want you to access this directly. 
    """

    __abc = 2
    """ 
    Private attribute - author doesn't want you to access this.
    """

    abc = 1
    """
    Normal attribute
    """


class Child(Perm):
    pass


def test_get_attributes():
    print(Child()._abc)
    print(Child().__abc)

# Having said that, having the convention of marking attributes as private or protected doesn't necessarily mean
# that you can't truly access the attributes; all private and protected attributes can be accessed.


def test_get_private_attribute():
    print(Child()._Perm__abc)

# test_get_private_attribute()
# test_get_attributes()
