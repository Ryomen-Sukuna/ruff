import abc

import pydantic


class Class:
    def badAllowed(self):
        pass

    def stillBad(self):
        pass

    if False:

        def badAllowed(self):
            pass

        def stillBad(self):
            pass

    @pydantic.validator
    def badAllowed(cls, my_field: str) -> str:
        pass

    @pydantic.validator
    def stillBad(cls, my_field: str) -> str:
        pass

    @pydantic.validator("my_field")
    def badAllowed(cls, my_field: str) -> str:
        pass

    @pydantic.validator("my_field")
    def stillBad(cls, my_field: str) -> str:
        pass

    @classmethod
    def badAllowed(cls):
        pass

    @classmethod
    def stillBad(cls):
        pass

    @abc.abstractclassmethod
    def badAllowed(cls):
        pass

    @abc.abstractclassmethod
    def stillBad(cls):
        pass


class PosOnlyClass:
    def badAllowed(self, blah, /, self, something: str):
        pass

    def stillBad(self, blah, /, self, something: str):
        pass
