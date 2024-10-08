import pytest
from design_patterns.behavioral.iterator import (
    ReturnEveryElementIterator,
    ReturnEveryOtherElementIterator,
    SequenceIterable,
)


@pytest.mark.parametrize("base_collection", [[1, 2, 3, 4, 5], "abcdefgh"])
@pytest.mark.parametrize("_reversed", [True, False])
def test_every_element_iterator(
    base_collection: list[int] | str, _reversed: bool
) -> None:
    iterable = SequenceIterable(
        base_collection=base_collection, iterator_type=ReturnEveryElementIterator
    )
    assert [value for value in (reversed(iterable) if _reversed else iterable)] == [
        value for value in (reversed(base_collection) if _reversed else base_collection)
    ]


@pytest.mark.parametrize(
    "base_collection", [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], "abcde" "abcdef"]
)
@pytest.mark.parametrize("_reversed", [True, False])
def test_every_other_element_iterator(
    base_collection: list[int] | str, _reversed: bool
) -> None:
    iterable = SequenceIterable(
        base_collection=base_collection, iterator_type=ReturnEveryOtherElementIterator
    )
    iteration_result = [
        value for value in (reversed(iterable) if _reversed else iterable)
    ]
    expected_iteration_result = []
    for index, value in enumerate(
        reversed(base_collection) if _reversed else base_collection
    ):
        if index % 2 == 0:
            expected_iteration_result.append(value)

    assert iteration_result == expected_iteration_result


@pytest.mark.parametrize(
    "base_collection,expected_length", [([1, 2, 3, 4, 5], 5), ("abcdefgh", 8)]
)
def test_len(base_collection: list[int] | str, expected_length: int) -> None:
    iterable = SequenceIterable(
        base_collection=base_collection, iterator_type=ReturnEveryElementIterator
    )

    assert len(iterable) == len(base_collection)


@pytest.mark.parametrize("base_collection", [[1, 2, 3, 4, 5], "abcdefgh"])
def test_get_item(base_collection: list[int] | str) -> None:
    iterable = SequenceIterable(
        base_collection=base_collection, iterator_type=ReturnEveryElementIterator
    )
    for index in range(len(iterable)):
        assert iterable[index] == base_collection[index]
