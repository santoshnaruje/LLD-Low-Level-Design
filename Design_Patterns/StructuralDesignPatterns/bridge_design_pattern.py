from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(Device):

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f"{self.name} {self.model}"

    def turn_on(self):
        print('TV turned on')

    def turn_off(self):
        print('TV turned off')


class Remote:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

if __name__ == '__main__':
    LG= TV("LG","UA8200")
    remote = Remote(LG)
    remote.turn_on()
    remote.turn_off()
