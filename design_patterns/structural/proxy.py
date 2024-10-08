from enum import auto, StrEnum
from abc import abstractmethod, ABC


class Permission(StrEnum):
    GRANTED = auto()
    DENIED = auto()


class PermissionDeniedError(Exception):
    pass


class Object(ABC):
    @abstractmethod
    def load(self) -> str: ...


class RawObject(Object):
    def load(self) -> str:
        return "object_loaded"


class ProtectionProxy(Object):
    def __init__(self, permission: Permission) -> None:
        self._protected_object = RawObject()
        self._permission = permission

    def load(self) -> str:
        if self._permission != Permission.GRANTED:
            raise PermissionDeniedError()
        return self._protected_object.load()
