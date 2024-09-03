import pytest
from typing import Type
from design_patterns.creation.singleton import SingletonTypeInt, SingletonTypeStr

@pytest.mark.parametrize("singleton_type,params", 
                         [(SingletonTypeInt, [1, 2]), (SingletonTypeStr, ["one", "two"])])
def test_singleton(singleton_type: Type[SingletonTypeInt | SingletonTypeStr],
                   params: list[int] | list[str]) -> None:
    instance_one = singleton_type(params[0])
    instance_two = singleton_type(params[1])

    assert instance_one.param == instance_two.param