# Button classes
class WindowsButton:
    def paint(self):
        print("Windows button")

class MacButton:
    def paint(self):
        print("Mac button")

# Checkbox classes
class WindowsCheckbox:
    def paint(self):
        print("Windows checkbox")

class MacCheckbox:
    def paint(self):
        print("Mac checkbox")

# Abstract factory
class UIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

# Concrete factories
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# usage
factory = WindowsFactory()
btn = factory.create_button()
chk = factory.create_checkbox()

btn.paint()
chk.paint()
