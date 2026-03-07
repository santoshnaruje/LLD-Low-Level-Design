from abc import ABC, abstractmethod


# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self,message):
        pass


# Subscriber
class EmailSubscriber(Observer):
    def update(self,message):
        print(f"Email subscriber called {message}")


class SmsSubscriber(Observer):
    def update(self,message):
        print(f"Sms subscriber called {message}")


# Subject

# Subject
class YoutubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == '__main__':
    channel = YoutubeChannel()
    email = EmailSubscriber()
    sms = SmsSubscriber()

    channel.subscribe(email)
    channel.subscribe(sms)

    channel.notify("Hello")

