class RealService:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def request(self):
        print(self.name)
        print(self.role)
        print("Request made successfully")

class ProxyService:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.service = RealService(name, role)

    def request(self):
        if self.role == "Admin":
            self.service.request()
        else:
            print(f"{self.name} with {self.role}has no service")


#Lazy loading
class Image:
    def display(self):
        print("Loading image from disk")


class ImageProxy:
    def __init__(self):
        self.image = None

    def display(self):
        if self.image is None:
            self.image = Image()

        self.image.display()




if __name__ == "__main__":
    service = ProxyService("Santosh", "Admin")
    service.request()
    service = ProxyService("Sanvan", "User")
    service.request()
    img = ImageProxy()
    img.display()
    img.display()
