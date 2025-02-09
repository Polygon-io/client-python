import inspect
import typing
from dataclasses import dataclass, asdict


_T = typing.TypeVar("_T")



def modelclass(cls: typing.Type[_T]) -> typing.Type[_T]:
    cls = dataclass(cls)
    attributes = [
        a
        for a in cls.__dict__["__annotations__"].keys()
        if not a.startswith("__") and not inspect.isroutine(a)
    ]

    def init(self, *args, **kwargs):
        for i, a in enumerate(args):
            if i < len(attributes):
                self.__dict__[attributes[i]] = a
        for k, v in kwargs.items():
            if k in attributes:
                self.__dict__[k] = v

    def to_dict(self):
        return asdict(self)

    cls.__init__ = init  # type: ignore[assignment]
    cls.to_dict = to_dict  # Add to_dict method to the class

    return cls