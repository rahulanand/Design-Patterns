from abc import ABC, abstractmethod
from typing import List

# Builder Pattern
# Encapsulate Construction of complex objects.

class AbstractNotifications(ABC):
    @abstractmethod
    def notify(self):
        pass


class NotifyGaurd(AbstractNotifications):
    def notify(self):
        print("Notifying Gaurd")
        print("Sending msg to gaurd")

class NotifyMember(AbstractNotifications):
    def notify(self):
        print("Notifying member")
        print("sending msg and email")

class NotifyHead(AbstractNotifications):
    def notify(self):
        print("Notifying Head")
        print("sending msg and email")

class AbstractBuilder(ABC):
    @abstractmethod
    def buildPart(self) -> List[AbstractNotifications]:
        pass

class Primary(AbstractBuilder):
    def buildPart(self):
        return [NotifyGaurd()]

class Secondary(AbstractBuilder):
    def buildPart(self):
        return [NotifyGaurd(), NotifyMember()]

class Tertiary(AbstractBuilder):
    def buildPart(self):
        return [NotifyGaurd(), NotifyMember(), NotifyHead()]
        


class Notifications(AbstractNotifications):
    _builder: AbstractBuilder
    _members: List[AbstractNotifications]

    def __init__(self, builder: AbstractBuilder) -> None:
        self._builder = builder
        self._members = self._builder.buildPart()

    def notify(self):
        for member in self._members:
            member.notify()


if __name__ == '__main__':
    # primary notfication
    print("========= Primary===========")
    primary = Notifications(Primary())
    primary.notify()

    # secondary
    print("=========Secondary===========")
    secondary = Notifications(Secondary())
    secondary.notify()

    # Tertiary
    print("=========Tertiary===========")
    tertiary = Notifications(Tertiary())
    tertiary.notify()

    




