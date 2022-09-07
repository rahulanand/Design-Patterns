from __future__ import annotations
from abc import ABC, abstractmethod
import time
import copy
import datetime

"""Prototype Pattern
"""

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Shopkeeper(Prototype):
    def __init__(self, height: int, age: int, defense: str, attack: str) -> None:
        time.sleep(3)
        self.height = height
        self.age = age
        self.defence = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30

    def clone(self):
        return copy.deepcopy(self)


class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        time.sleep(3)
        self.height = height
        self.age = age
        self.defence = defense
        self.attack = attack
        # Concrete class attribute
        self.stamina = 60
    # Overwritting Cloning Method
    def clone(self):
        return copy.deepcopy(self) 


if __name__ == "__main__":
    # without using clone method
    print('Starting to create a Shopkeeper NPC: ', datetime.datetime.now().time())
    shopkeeper = Shopkeeper(180, 22, 5, 8)
    print('Finished creating a Shopkeeper NPC: ', datetime.datetime.now().time())
    print('Attributes: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

    
    print('Instantiating trader guild at: ', datetime.datetime.now().time())
    shopkeeper_template = Shopkeeper(180, 22, 5, 8)
    #Using clone method
    for i in range(5):
        shopkeeper_clone = shopkeeper_template.clone()
        print(f'{id(shopkeeper_clone)} : Finished creating a Shopkeeper clone {i} at: ', datetime.datetime.now().time())
    print('Finished instantiating trader guild at: ', datetime.datetime.now().time())