from assertpy import assert_that, soft_assertions
from design_patterns.behavioral.template_method import Derived


def test_template_method() -> None:
    object_under_test = Derived()
    return_value = object_under_test.do_work()

    with soft_assertions():  # type: ignore
        assert_that(return_value).is_equal_to(12)
        assert_that(object_under_test).has__hook_result(2)
        assert_that(object_under_test).has__do_work_result(10)
