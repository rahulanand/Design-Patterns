from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum

"""Flyweight Pattern.
   Usage: When one instance of a class can be used to provide many virtual instances. (Saving memory) 
"""

class Color(Enum):
    RED=1
    BLUE=2
    GREY=3


class Shape(ABC):
    _color: Color  # Intrinsic property : immutable

    @abstractmethod
    def draw(self, x: int, y: int):  # extrinsisc property: Mutable based on x and y
        pass

class Rectangle(Shape):
    def __init__(self, color: str) -> None:
        self._color = color

    def draw(self, x: int, y: int):
        print(f"Drawing rectangle of color {self._color} on coordinates x: {x} and y: {y}")


class RectangleFactory:
    __store: Dict[str, Rectangle] = {}

    @staticmethod
    def getRectangle(color: str):
        store = RectangleFactory._RectangleFactory__store
        if color not in store:
            print(f"Creating new object of color: {color}")
            store[color] = Rectangle(color)
        return store[color]


if __name__ == "__main__":

    for color in Color:
        rect = RectangleFactory.getRectangle(color.name)
        rect.draw(10, 10)

    # For below, no new objects will be created same object will be reused.

    rect = RectangleFactory.getRectangle("RED")
    rect.draw(50, 40)

    rect = RectangleFactory.getRectangle("BLUE")
    rect.draw(30, 40)

    rect = RectangleFactory.getRectangle("GREY")
    rect.draw(70, 40)


