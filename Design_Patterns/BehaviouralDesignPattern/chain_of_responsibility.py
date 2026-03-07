class Handler:
    def __init__(self, handler=None):
        self.next_handler = handler

    def handle(self, request):
        if self.next_handler is not None:
            self.next_handler.handle(request)
        return None


class LogHandler(Handler):
    def handle(self, request):
        print("I am logging the request object", request)
        return super().handle(request)


class AuthHandler(Handler):
    def handle(self, request):
        if request.get("role" ,None)== 'Admin':
            print("You are logged in as a Admin user", request)
            return super().handle(request)
        print("You are not logged in as a Admin user", request)
        return False


class ResponseHandler(Handler):
    def handle(self, request):
        print("I am Responding to the request object", request)
        print ("End of the request")
        return "True"

if __name__ == '__main__':

    chain = LogHandler(AuthHandler(ResponseHandler()))

    request = {
        "name":"Santosh Naruje",
        "designation":"Software developer",
        "role":"santosh"
    }

    chain.handle(request)