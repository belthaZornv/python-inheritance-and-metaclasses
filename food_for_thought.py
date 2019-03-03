# When subclassing, do you expect instances of a subclass to compare equal to instances of their parent?
# Assume that __eq__ is inherited, rather than overridden or extended.


class A:
    pass


class B(A):
    pass

# A(a, b) == B(a, b)
