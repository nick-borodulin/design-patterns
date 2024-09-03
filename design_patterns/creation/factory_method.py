from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        ...

class Truck(Transport):
    def deliver(self) -> str:
        return "deliver_by_truck"
    
class Ship(Transport):
    def deliver(self) -> str:
        return "deliver_by_ship"
    
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        ...
    
    def deliver(self) -> str:
        return self.create_transport().deliver()

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()
    
class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

