from abc import ABC, abstractmethod
from typing import List
import random


class State(ABC):
    @abstractmethod
    def insertQuarter(self):
        pass

    @abstractmethod
    def ejectQuarter(self):
        pass

    @abstractmethod
    def turnCrank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class NoQuarterState(State):
    gumballMachine = None

    def __init__(self, gumballMachine) -> None:
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You inserted a quarter.")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter.")

    def turnCrank(self):
        print("You turned but there is no quarter.")

    def dispense(self):
        print("you need to pay first")


class HasQuarterState(State):
    gumballMachine = None

    def __init__(self, gumballMachine) -> None:
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("You can;t insert another quarter.")

    def ejectQuarter(self):
        print("Quarter returned.")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("You turned....")
        winner = random.randint(0,10)
        if winner == 0 and self.gumballMachine.getCount() > 1:
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("No gumball dispensed.")


class SoldState(State):
    gumballMachine = None

    def __init__(self, gumballMachine) -> None:
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we are already giving you a gumball.")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank.")

    def turnCrank(self):
        print("Turning twice, invalid")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Ooops, out of gumballs!!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class SoldOutState(State):
    gumballMachine = None

    def __init__(self, gumballMachine) -> None:
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("can't insert quarter")

    def ejectQuarter(self):
        print("No quarter")

    def turnCrank(self):
        print("not valid")

    def dispense(self):
        print("not valid")


class WinnerState(State):
    gumballMachine = None

    def __init__(self, gumballMachine) -> None:
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("can't insert")

    def ejectQuarter(self):
        print("can't eject")

    def turnCrank(self):
        print("can't trunk")

    def dispense(self):
        self.gumballMachine.releaseBall()

        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            print("You're a winner!!!, you got two gumballs")
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Ooops out of gumballs.")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


class GumballMachine:
    soldOutState: State
    noQuarterState: State
    hasQuarterState: State
    soldState: State
    winnerState: State

    state: State
    count: int = 0

    def __init__(self, count: int) -> None:
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)

        self.count = count
        if count > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self, state: State):
        self.state = state

    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def getCount(self):
        return self.count

    def getSoldOutState(self):
        return self.soldOutState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    def getWinnerState(self):
        return self.winnerState

    def __str__(self) -> str:
        return "Current state: " + str(self.state)


if __name__ == "__main__":
    gumballMachine = GumballMachine(5)
    print(str(gumballMachine))

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(str(gumballMachine))

    gumballMachine.insertQuarter()
    gumballMachine.ejectQuarter()

    gumballMachine.turnCrank()
    
    print(str(gumballMachine))

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.ejectQuarter()
    
    print(str(gumballMachine))
    
    gumballMachine.insertQuarter()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    
    print(str(gumballMachine))


