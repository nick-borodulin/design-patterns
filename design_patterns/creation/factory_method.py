"""
This is the most used design pattern, Factory Method. Logisitics is the interface class, which can deliver using Truck or Ship.
You would choose either RoadLogistics or SeaLogistics and just say "deliver".
"""

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str: ...


class Truck(Transport):
    def deliver(self) -> str:
        return "deliver_by_truck"


class Ship(Transport):
    def deliver(self) -> str:
        return "deliver_by_ship"


class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport: ...

    def deliver(self) -> str:
        return self.create_transport().deliver()


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
