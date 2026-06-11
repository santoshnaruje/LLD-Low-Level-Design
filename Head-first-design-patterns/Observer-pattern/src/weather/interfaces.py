from abc import ABC, abstractmethod


class Subject(ABC):
    """Subject (Observable) interface: defines methods to manage and notify observers."""

    @abstractmethod
    def register_observer(self, o: "Observer") -> None:
        """Register an observer so it can receive state updates."""
        pass

    @abstractmethod
    def remove_observer(self, o: "Observer") -> None:
        """Remove an observer so it stops receiving state updates."""
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """Notify all registered observers when the Subject's state changes."""
        pass


class Observer(ABC):
    """Observer interface: all observer components must implement this."""

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        """Called by the Subject when its state changes, passing new measurements."""
        pass


class DisplayElement(ABC):
    """Display interface: implemented by all display elements in the Weather Station."""

    @abstractmethod
    def display(self) -> None:
        """Renders/displays the weather measurements on the screen."""
        pass
