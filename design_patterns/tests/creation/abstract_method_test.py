from design_patterns.creation.factory_method import RoadLogistics, SeaLogistics


def test_road_logistics():
    logistics = RoadLogistics()
    assert logistics.deliver() == "deliver_by_truck"


def test_sea_logistics():
    logistics = SeaLogistics()
    assert logistics.deliver() == "deliver_by_ship"
