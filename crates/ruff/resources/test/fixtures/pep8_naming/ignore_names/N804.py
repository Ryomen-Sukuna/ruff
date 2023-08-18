from abc import ABCMeta


class Class:
    def __init_subclass__(cls, default_name, **kwargs):
        ...

    @classmethod
    def badAllowed(cls, x, /, other):
        ...

    @classmethod
    def stillBad(cls, x, /, other):
        ...


class MetaClass(ABCMeta):
    def badAllowed(self):
        pass

    def stillBad(self):
        pass
