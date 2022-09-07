from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum

"""Interpreter Pattern.
"""

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context: str) ->bool:
        pass

class TerminalExpression(AbstractExpression):
    _data: str = ""

    def __init__(self, data: str) -> None:
        self._data = data

    def interpret(self, context: str) -> bool:
        if self._data in context:
            return True
        return False


class OrExpression(AbstractExpression):
    _expr1: AbstractExpression = None
    _expr2: AbstractExpression = None

    def __init__(self, expr1: AbstractExpression, expr2: AbstractExpression) -> None:
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context: str) -> bool:
        return self._expr1.interpret(context) or self._expr2.interpret(context)


class AndExpression(AbstractExpression):
    _expr1: AbstractExpression = None
    _expr2: AbstractExpression = None

    def __init__(self, expr1: AbstractExpression, expr2: AbstractExpression) -> None:
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context: str) -> bool:
        return self._expr1.interpret(context) and self._expr2.interpret(context)


if __name__ == "__main__":
    person1 = TerminalExpression("Kushagra")
    person2 = TerminalExpression("Lokesh")

    isSingle = OrExpression(person1, person2)
          
    vikram = TerminalExpression("Vikram")
    committed = TerminalExpression("Committed")
    isCommitted = AndExpression(vikram, committed)    
  
    print(isSingle.interpret("Kushagra"))
    print(isSingle.interpret("Lokesh"))
    print(isSingle.interpret("Achint"))
          
    print(isCommitted.interpret("Committed, Vikram"))
    print(isCommitted.interpret("Single, Vikram"))





