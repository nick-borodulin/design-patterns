import pytest
from design_patterns.structural.composite import Component, Composite, InvalidLeafError, Leaf

def test_composite_with_leafs() -> None:
    components: list[Component] = [Leaf(), Leaf()]
    composite = Composite()
    composite.add_child(Leaf())
    composite.add_child(Leaf())
    components.append(composite)

    result_of_operations = "".join(component.operation() for component in components)
    assert result_of_operations == "child_operation" * 2 + "composite_operation" + "child_operation" * 2

def test_composite_with_no_leafs() -> None:
    composite = Composite()
    assert composite.operation() == "composite_operation"

def test_leaf_removal() -> None:
    composite = Composite()
    leaf = Leaf()
    composite.add_child(leaf)
    assert composite.operation() == "composite_operation" + "child_operation"

    composite.remove_child(leaf)
    assert composite.operation() == "composite_operation"

def test_invalid_leaf_removal() -> None:
    composite = Composite()
    composite.add_child(Leaf())

    assert len(composite._children) == 1

    with pytest.raises(InvalidLeafError): 
        composite.remove_child(Leaf())

    assert len(composite._children) == 1