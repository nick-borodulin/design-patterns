from pytest import raises
from design_patterns.structural.proxy import Permission, PermissionDeniedError, ProtectionProxy

def test_permission_granted() -> None:
    proxy = ProtectionProxy(Permission.GRANTED)
    assert proxy.load() == "object_loaded"

def test_permission_denied() -> None:
    proxy = ProtectionProxy(Permission.DENIED)
    with raises(PermissionDeniedError):
        proxy.load()