from abc import ABC, abstractmethod

# Abstract Pizza store class can have multiple pizza stores (subclass)
# which will implement the factory method createPizza()

class Pizza(ABC):
    name = None
    dough = None
    sauce = None
    toppings = []

    def prepare(self):
        print("Preparing: ", self.name)
        print("Tossing: ", self.dough)
        print("Adding Sauce: ", self.sauce)
        print("Adding Toppings: ")
        for t in self.toppings:
            print(t + " topping")
    
    def bake(self):
        print("Baking for 25 minutes")

    def cut(self):
        print("Cutting pizza..")

    def box(self):
        print("Placing pizza in abox")

    def getName(self):
        return self.name

class PizzaStore(ABC):

    def orderPizza(self, type):
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def createPizza(self, type):
        pass

class NYPizzaStore(PizzaStore):

    def createPizza(self, type):
        if type == "cheese":
            return NYStyleCheesePizza()


class NYStyleCheesePizza(Pizza):
    name = "NY Style suce and cheese pizza"
    dough = "Thin Crust Dough"
    sauce = "Marianara suce"
    toppings = ["Ragginao cheese"]



pizza_store = NYPizzaStore()
pizza_store.orderPizza("cheese")