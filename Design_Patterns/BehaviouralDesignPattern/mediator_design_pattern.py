class ChatMediator:
    def __init__(self):
        self.logs = []

    def send(self, user, message):
        self.logs.append((user, message))
        print(f"[{user}] says: {message}")


class User:
    def __init__(self, name):
        self.name = name
        self.mediator = ChatMediator()

    def sendMessage(self,message):
        self.mediator.send(self.name,message)

if __name__ == "__main__":
    user1 = User("Santosh")
    user2 = User("Sanvan")
    user3 = User("Naruje")

    user1.sendMessage("Hello")
    user2.sendMessage("Hello Santosh")
    user3.sendMessage("Hello Naruje")
    user1.sendMessage("How are you doing")
    user2.sendMessage("I am good how are you")
    user3.sendMessage("I am fine what about you")