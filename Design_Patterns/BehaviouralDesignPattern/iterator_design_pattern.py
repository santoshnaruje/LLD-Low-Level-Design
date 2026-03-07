from abc import ABC, abstractmethod


class Iterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class ListIterator(Iterator):

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item
        return None


class MyCollection:

    def __init__(self, items):
        self.items = items

    def create_iterator(self):
        return ListIterator(self.items)


if __name__ == "__main__":
    collection = MyCollection([1, 2, 3, 4, 5])
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(iterator.next())
