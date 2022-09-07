from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

# Chain of responsibility pattern
# Each object in turn examines a request and either handles it 
# or passes it on to the next object in the chain.

class Handler(ABC):
    @abstractmethod
    def setNext(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) ->Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def setNext(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "banana":
            return f"Monkey: will handle this {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "nut":
            return f"Squirrel: will handle this {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "meatBall":
            return f"Dog: will handle this request {request}"
        else:
            super().handle(request)


if __name__ == "__main__":
    monkey, suirrel, dog = MonkeyHandler(), SquirrelHandler(), DogHandler()
    
    # set chain of handler
    # monkey -> suirrel -> dog
    monkey.setNext(suirrel).setNext(dog)

    for food in ["nut", "banana", "meatBall", "coffe"]:
        print(monkey.handle(food))





    




