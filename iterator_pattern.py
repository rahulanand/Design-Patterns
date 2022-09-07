from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import List

class MenuItem:
    name: str
    description: str
    vegeterian: bool
    price: float

    def __init__(self, name, description, vegeterian, price) -> None:
        self.name = name
        self.description = description
        self.vegeterian = vegeterian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def isVegeterian(self):
        return self.vegeterian

class DinerMenuIterator(Iterator):
    items: List[MenuItem]
    position = 0

    def __init__(self, items: List[MenuItem]) -> None:
        self.items = items

    def __next__(self):
        if self.position >= len(self.items):
            raise StopIteration
        item = self.items[self.position]
        self.position += 1
        return item

class DinerMenu:
    MAX_ITEMs = 6
    menuItems: List[MenuItem] = []

    def __init__(self) -> None:
        self.addItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT", "Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("Soup of the day", "Soup of the day, with a side of potato salad", True, 3.29)
        self.addItem("Hotdog", "A hot dog, with sauerkraut, relish, onions, topped with cheese", True, 3.05)

    def addItem(self, name, description, vegeterian, price):
        self.menuItems.append(MenuItem(name, description, vegeterian, price))

    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

class Waitress:
    dinerMenu: DinerMenu

    def __init__(self, dinerMenu: DinerMenu) -> None:
        self.dinerMenu = dinerMenu

    def printMenu(self):
        iterator = self.dinerMenu.createIterator()
        print("================Menu==============")
        for item in iterator:
            print(item.getName(), item.getDescription(), "Veg: ", item.isVegeterian(), item.getPrice())

if __name__ == '__main__':
    waitress = Waitress(DinerMenu())
    waitress.printMenu()
