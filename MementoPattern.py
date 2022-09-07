from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

"""The Memento's principle can be achieved using serialization.
"""

class Memento(ABC):
    @abstractmethod
    def get_name(self) ->str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class Originator:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Intial state: {self._state}")

    def do_something(self) -> None:
        self._state = self._generate_random_string(30)
        print(f"Originator: state changed to {self._state}")

    def _generate_random_string(self, length: int=10):
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento
        print(f"Originator: state changed to {self._state}")


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._mementos = []

    def backup(self):
        print("Saving originator state")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not self._mementos:
            return
        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: List of mementos: ")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("super-duper")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

