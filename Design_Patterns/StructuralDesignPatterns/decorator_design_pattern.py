
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        func(*args, **kwargs)
        print("After call")
    return wrapper



@log_decorator
def process_payment(amount):
    print(amount)


if __name__ == '__main__':
    process_payment(100)