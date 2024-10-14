from assertpy import assert_that
from design_patterns.behavioral.memento import Originator, Caretaker


def test_memento() -> None:
    originator = Originator()
    caretaker = Caretaker(originator=originator)
    assert_that(caretaker._history).is_empty()
    originator.do_work()
    caretaker.backup()
    assert_that(caretaker._history).is_not_empty()
    assert_that(caretaker._history).contains_only(originator._state)
    originator.do_work()
    assert_that(caretaker._history).is_length(2)
    memento = caretaker._history[-1]
    caretaker.undo()
    assert_that(caretaker._history).is_length(1)
    assert_that(originator._state).is_equal_to(memento)
