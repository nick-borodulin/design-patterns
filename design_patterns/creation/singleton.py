from threading import Lock
from typing import Any


class SingletonMetaClass(type):
    _lock = Lock()
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwds)
            return cls._instances[cls]


class SingletonTypeInt(metaclass=SingletonMetaClass):
    def __init__(self, param: int) -> None:
        self._param = param

    @property
    def param(self) -> int:
        return self._param


class SingletonTypeStr(metaclass=SingletonMetaClass):
    def __init__(self, param: str) -> None:
        self._param = param

    @property
    def param(self) -> str:
        return self._param
