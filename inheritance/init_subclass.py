class A:
    def __init_subclass__(cls, registry=None, **kwargs):
        if isinstance(registry, list):
            registry.append(cls)
            cls.registered_in = registry


registry = []


# note the variables are already defined at import/declaration time
# it maybe a constant like a configuration object or a mutable object.
class B(A, registry=registry):
    def __init__(self):
        pass


# Like metaclasses everything happens when declaring the subclass
assert registry == B.registered_in == [B]


# Introduced in 3.6+
# Check https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__

# PEP 487 sets out to take two common metaclass usecases and make them more accessible without having to understand all the ins and outs of metaclasses. The two new features, __init_subclass__ and __set_name__ are otherwise independent, they don't rely on one another.
#
# __init_subclass__ is just a hook method. You can use it for anything you want. It is useful for both registering subclasses in some way, and for setting default attribute values on those subclasses.
#
# We recently used this to provide 'adapters' for different version control systems, for example:

class RepositoryType(Enum):
    HG = 'hg'
    GIT = 'git'
    SVN = 'svn'
    PERFORCE = 'perf'


class Repository:
    _registry = {t: {} for t in RepositoryType}

    def __init_subclass__(cls, scm_type=None, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if scm_type is not None:
            cls._registry[scm_type][name] = cls


class MainHgRepository(Repository, scm_type=RepositoryType.HG, name='main'):
    pass


class GenericGitRepository(Repository, scm_type=RepositoryType.GIT, name='generic'):
    pass

# This trivially let us define handler classes for specific repositories without having to resort to using a metaclass or decorators.
