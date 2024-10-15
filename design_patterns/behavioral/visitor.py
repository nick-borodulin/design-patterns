"""
Visitor pattern is usused when you have a set of classes with a common parent (in this example, Equipment, Bulb, Drill)
and a you need to do a set of actions on each of them, where the action depends on the type. An alternative approach would
be modifying the interfact (Equipment) by including a new abstract method, but that's not the best approach because
with each new feature you'd have to modify all the classes in the hierarchy. Instead, this logic is put into a new type of 
Visitor. In the example below we have 2 visitors: CostVisitor that calculates total cost of all the equipment, and
PowerConsumptionVisitor that calculates total power consumption. In additition to not having to modify all the classes of 
the main hierarchy, we are able to accumulate the cost/power consumption in the visitor class. Had we used the "naive" approach,
we'd have to keep track of it outside, in the client code.
Visitor pattern uses "double-dispatch" technique. It means that a piece of code that's being executed is determined by two
criteria - the type of the visitor and the type of the main hierarchy class.
"""

from abc import ABC, abstractmethod
from typing import Any


class Visitor(ABC):
    @abstractmethod
    def visit_bulb(self, bulb: "Bulb") -> None: ...

    @abstractmethod
    def visit_drill(self, drill: "Drill") -> None: ...


class Equipment(ABC):
    @property
    @abstractmethod
    def full_price(self) -> float: ...

    @property
    @abstractmethod
    def discount_price(self) -> float: ...

    @property
    @abstractmethod
    def watt_power(self) -> float: ...

    @abstractmethod
    def accept(self, visitor: Visitor) -> Any: ...


class Bulb(Equipment):
    @property
    def full_price(self) -> float:
        return 10.0

    @property
    def discount_price(self) -> float:
        return 9.0

    @property
    def watt_power(self) -> float:
        return 20.0

    def accept(self, visitor: Visitor) -> Any:
        return visitor.visit_bulb(self)


class Drill(Equipment):
    @property
    def full_price(self) -> float:
        return 100.0

    @property
    def discount_price(self) -> float:
        return 80.0

    @property
    def watt_power(self) -> float:
        return 200.0

    def accept(self, visitor: Visitor) -> Any:
        return visitor.visit_drill(self)


class CostVisitor(Visitor):
    def __init__(self) -> None:
        self._total_cost: float = 0.0

    def visit_bulb(self, bulb: Bulb) -> None:
        self._total_cost += bulb.full_price

    def visit_drill(self, drill: Drill) -> None:
        self._total_cost += drill.discount_price

    @property
    def total_cost(self) -> float:
        return self._total_cost


class PowerConsumptionVisitor(Visitor):
    def __init__(self) -> None:
        self._total_watt_power: float = 0.0

    def visit_bulb(self, bulb: Bulb) -> None:
        self._total_watt_power += bulb.watt_power

    def visit_drill(self, drill: Drill) -> None:
        self._total_watt_power += drill.watt_power

    @property
    def total_watt_power(self) -> float:
        return self._total_watt_power
