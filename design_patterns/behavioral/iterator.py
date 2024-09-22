from operator import contains
from typing import Sequence, Iterator, Type, TypeVar

T = TypeVar("T")

class IteratorBase(Iterator[T]):
    def __init__(self, collection: Sequence[T], reversed: bool=False) -> None:
        super().__init__()
        self._collection = collection
        self._position = -1 if reversed else 0
        self._reversed = reversed


class ReturnEveryElementIterator(IteratorBase[T]):
    """
    A "regular" iterator which returns every element of the collection.
    """    
    def __next__(self) -> T:
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reversed else 1
            return value
        except IndexError:
            raise StopIteration


class ReturnEveryOtherElementIterator(IteratorBase[T]):
    """
    An iterator that returns every other element of the collection.
    """
    def __next__(self) -> T:
        try:
            value = self._collection[self._position]
            self._position += -2 if self._reversed else 2
            return value
        except IndexError:
            raise StopIteration


class SequenceIterable(Sequence[T]):
    """
    Inherits from Sequence - IteratorBase assumes that the |SequenceIterable|
    is a list-like object.
    """
    def __init__(self,
                 base_collection: Sequence[T],
                 iterator_type: Type[IteratorBase[T]]) -> None:
        self._base_collection = base_collection
        self._iterator_type = iterator_type

    def __getitem__(self, index: int) -> T: # type: ignore (Pylance is not recognizing @override)
        return self._base_collection[index]

    def __len__(self) -> int:
        return len(self._base_collection)

    def __iter__(self) -> IteratorBase[T]:
        return self._iterator_type(self, reversed=False)
    
    def __reversed__(self) -> Iterator[T]:
        return self._iterator_type(self, reversed=True)

    def __contains__(self, value: object) -> bool:
        return contains(self._base_collection, value)