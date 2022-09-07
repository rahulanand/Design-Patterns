from abc import ABC, abstractmethod
from os import remove
from typing import List

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is on")
    
    def off(self):
        print("Light is Off")

class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self):
        self.light.off()

class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self):
        self.light.on()


class RemoteControl:
    onCommands: List
    offCommands: List
    remoteSize: int

    def __init__(self, remoteSize: int) -> None:
        # Initialize commands with None
        self.remoteSize = remoteSize
        self.onCommands = [None] * remoteSize
        self.offCommands = [None] * remoteSize

    def setCommand(self, slot: int, onCommand: Command, offCommand: Command) -> None:
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonPushed(self, slot: int) -> None:
        self.onCommands[slot].execute()

    def offButtonPushed(self, slot: int) ->None:
        self.offCommands[slot].execute()

    def __str__(self) ->str:
        str = "\n Remote Control Commands: \n"
        for i in range(self.remoteSize):
            str += "[SLOT] %d commands: %s \n" %(i, self.onCommands[i])
        return str

remote = RemoteControl(1)
light = Light()
remote.setCommand(0, LightOnCommand(light), LightOffCommand(light))
print(str(remote))
remote.onButtonPushed(0)
remote.offButtonPushed(0)