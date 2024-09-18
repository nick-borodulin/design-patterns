from abc import ABC, abstractmethod
from time import sleep


class Observer(ABC):
    @abstractmethod
    def update(self, subject: "Subject") -> None:
        ...

class Subject(ABC):
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach_observer(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

class Timer(Subject):
    def __init__(self, seconds: float) -> None:
        super().__init__()
        self._timer_seconds = seconds

    def start(self) -> None:
        sleep(self._timer_seconds)
        self.notify()


class Clock(Observer):
    def __init__(self, timer: Timer) -> None:
        self._timer = timer
        self._timer.attach_observer(self)
        self._timer_went_off = False

    @property
    def timer_went_off(self) -> bool:
        return self._timer_went_off

    def update(self, subject: Subject) -> None:
        if subject is self._timer:
            self._timer_went_off = True


