class A:
    def func(self):
        print('A')


class B:
    def func(self):
        print('B')


class C:
    def func(self):
        print('C')


class Child(A, B, C):
    pass


print(Child().func)
print(Child.mro())

# `func` is bound to which class?
# What's a bound method?
# A bound method is essentially a method that belongs to an instance.