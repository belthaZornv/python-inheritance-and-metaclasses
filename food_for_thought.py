# When subclassing, do you expect instances of a subclass to compare equal to instances of their parent?
# Assume that __eq__ is inherited, rather than overridden or extended.

from math import sqrt, pow

class PlaneNorm:
    def __init__(self, x: int, y: int):
        """ 
        Note that we could use attrs or dataclass (3.7 only) to avoid writing the init
        """
        self.x = x
        self.y = y
    
    def euclid_norm(self):
        """ 
        In the plane we use the radius of the zero-centered circonference in which the point exists. 
        """
        return sqrt(pow(self.x, 2) + pow(self.y, 2))
        
    def __eq__(self, other: 'PlaneNorm'):
        """ EQ is only about the norm being equal """
        return self.euclid_norm() == other.euclid_norm()


class SpaceNorm(A):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def euclid_norm(self):
        """ 
        In the space we use the radius of the zero-centered sphere in whose surface the point exists.
        """
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

x = 1
y = 2

# we can still compare the two different classes
assert PlaneNorm(x, y) == SpaceNorm(x, y, 0)

# note tha you can never use IS as it works on the identity of the object
assert PlaneNorm(x, y) is not PlaneNorm(x, y)
