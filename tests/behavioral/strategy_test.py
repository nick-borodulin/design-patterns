from typing import Type, TypeVar
import pytest
from design_patterns.behavioral.strategy import Context, RemoveHead, RemoveTail

T = TypeVar("T", int, str)

def _generate_expected_output(input_list: list[T],
                              strategy_class: Type[RemoveHead | RemoveTail]) -> list[T]:
    expected_output = []
    if input_list:
        if strategy_class is RemoveHead:
            expected_output = input_list[1:]
        else:
            expected_output = input_list[:-1]
    return expected_output
    
@pytest.mark.parametrize("input_list", [
                         [1,2,3],
                         ["one", "two"],
                         []
])
@pytest.mark.parametrize("strategy_class", [RemoveHead, RemoveTail])
def test_remove_head(input_list: list[T],
                     strategy_class: Type[RemoveHead | RemoveTail]) -> None:
    context = Context(strategy_class())
    expected_output = _generate_expected_output(input_list=input_list,
                                                strategy_class=strategy_class)
    
    return_list = context.business_logic(input_list)
    assert return_list == expected_output
    