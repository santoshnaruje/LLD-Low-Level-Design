import threading


class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

class MultiThreadedDatabase():
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = object.__new__(cls)
            return cls._instance

def create_db():
    db = Database()
    print(id(db))

if __name__ == '__main__':
    threads = []

    for _ in range(5):
        t = threading.Thread(target=create_db)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()




