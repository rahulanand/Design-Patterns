from abc import ABC, abstractmethod

"""
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, 
all of its dependents are notified and updated automatically.
(Page 51). 
"""

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class WeatherData(Subject):
    __observers = []
    __temperature = None
    __humidity = None
    __pressure = None

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    @property
    def pressure(self):
        return self.__pressure

    def registerObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update()
    
    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temp, humid, pressure):
        self.__temperature = temp
        self.__humidity = humid
        self.__pressure = pressure
        self.measurementsChanged()

class currentConditionsDisplay(Observer, DisplayElement):
    __temperature = None
    __humidity = None
    __weatherData = None

    def __init__(self, data):
        self.__weatherData = data
        data.registerObserver(self)

    def update(self):
        self.__temperature = self.__weatherData.temperature
        self.__humidity = self.__weatherData.humidity
        self.display()

    def display(self):
        print("Current condition: temperature: %s , humidity: %s" %(self.__temperature, self.__humidity))

waether_data = WeatherData()
current_display = currentConditionsDisplay(waether_data)

waether_data.setMeasurements(10, 10, 10)
waether_data.setMeasurements(10, 14, 20)
waether_data.setMeasurements(20, 30, 10)

