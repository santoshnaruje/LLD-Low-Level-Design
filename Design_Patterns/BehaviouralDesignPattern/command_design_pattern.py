from abc import ABC


# Command Interface
class Command(ABC):
    def execute(self):
        pass

# Receiver
class Light:

    def turn_on(self):
        print("Light is turn on")

    def turn_off(self):
        print("Light is turn off")

# Concrete Commands
class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker
class RemoteControl(Command):

    def __init__(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


if __name__ == '__main__':
    light = Light()

    on_command = LightOnCommand(light)

    off_command = LightOffCommand(light)

    remote = RemoteControl(on_command)
    remote.press_button()

    remote = RemoteControl(off_command)
    remote.press_button()
