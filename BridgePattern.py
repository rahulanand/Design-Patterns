from abc import ABC, abstractmethod

# Bridge-Pattern

# Implementor
class DrawAPI(ABC):
    @abstractmethod
    def draw(self):
        pass

# Creating Concrete Implementor
class DrawRed(DrawAPI):
    def draw(self):
        print("Drawing Red.")

class DrawBlue(DrawAPI):
    def draw(self):
        print("Drawing blue.")

# Abstraction class
class Shape(ABC):
    drawAPI: DrawAPI
    def __init__(self, drawAPI: DrawAPI) -> None:
        self.drawAPI = drawAPI

    @abstractmethod
    def draw(self):
        pass

# Creating concrete abstraction
class Circle(Shape):
    def __init__(self, drawAPI: DrawAPI) -> None:
        super().__init__(drawAPI)

    def draw(self):
        self.drawAPI.draw()


if __name__ == "__main__":
    # Red circle
    redCircle = Circle(DrawRed())
    redCircle.draw()

    # Blue circle
    blueCircle = Circle(DrawBlue())
    blueCircle.draw()



