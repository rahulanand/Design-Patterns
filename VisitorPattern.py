from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

"""Visitor Pattern.
   - The Visitor pattern suggests that you place the new behavior into a separate class called visitor, 
      instead of trying to integrate it into existing classes.
"""

class Visitor(ABC):
    @abstractmethod
    def visit_component_a(self, element: ComponentA) -> None:
        pass

    @abstractmethod
    def visit_component_b(self, element: ComponentB) -> None:
        pass


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ComponentA(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_a(self)

    def other_method(self) -> str:
        return "A"

class ComponentB(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_component_b(self)

    def other_method(self) -> str:
        return "B"


class ConcreteVisitor1(Visitor):
    def visit_component_a(self, element) -> None:
        print(f"{element.other_method()} + ConcreteVisitor1")

    def visit_component_b(self, element) -> None:
        print(f"{element.other_method()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_component_a(self, element) -> None:
        print(f"{element.other_method()} + ConcreteVisitor2")

    def visit_component_b(self, element) -> None:
        print(f"{element.other_method()} + ConcreteVisitor2")

def client_code(components: List[Component], visitor: Visitor) -> None:
    """
    The client code can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    # ...
    for component in components:
        component.accept(visitor)
    # ...


if __name__ == "__main__":
    components = [ComponentA(), ComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)