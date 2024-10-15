from assertpy import assert_that
from design_patterns.behavioral.visitor import (
    Bulb,
    CostVisitor,
    Drill,
    PowerConsumptionVisitor,
)


def test_cost_visitor() -> None:
    visitor = CostVisitor()
    equipment = 2 * [Bulb()] + 3 * [Drill()]
    for item in equipment:
        item.accept(visitor=visitor)

    assert_that(visitor.total_cost).is_equal_to(260.0)


def test_power_consumption_visitor() -> None:
    visitor = PowerConsumptionVisitor()
    equipment = 2 * [Bulb()] + 3 * [Drill()]
    for item in equipment:
        item.accept(visitor=visitor)

    assert_that(visitor.total_watt_power).is_equal_to(640.0)
