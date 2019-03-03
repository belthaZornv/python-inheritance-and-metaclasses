def global_example():
    """
    global example
    :return:
    """
    global attr_global

    attr_global = 10


attr_global = 1

global_example()
assert attr_global == 10


def closure_example():
    """
    nonlocal example inside a closure
    :return:
    """
    attr_non_local = 10

    def closure():
        nonlocal attr_non_local

        attr_non_local = 20

        return attr_non_local

    return closure()


assert closure_example() == 20

# What's a closure?
# Focus: Inheritance (C3, How _, __ affects inheritance, Bound to what?)
# Focus: Metaclasses (What's the purpose of using metaclasses? why? use case and build)
# Focus: Mixins (What's the purpose of using a mixin? use case and build)
