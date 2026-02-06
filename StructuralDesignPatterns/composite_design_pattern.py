class FileSystem:
    def show(self):
        pass


class File(FileSystem):
    def __init__(self, filename):
        self.filename = filename

    def show(self, indent=0):
        return (" " * indent) + self.filename


class Directory(FileSystem):
    def __init__(self, directory_name):
        self.directory_name = directory_name
        self.items = []

    def add_file(self, item):
        self.items.append(item)

    def show(self,indent=0):
        result = (" " * indent) + self.directory_name  + "\n"
        for item in self.items:
            result += item.show(indent + 4) + "\n"
        return result.rstrip()


if __name__ == '__main__':
    file1 = File('file1.txt')
    file2 = File('file2.txt')
    directory3 = Directory('Directory.txt')
    file3 = File('file3.txt')
    directory1 = Directory('directory1')
    directory2 = Directory('directory2')
    directory3.add_file(file3)
    directory1.add_file(directory3)
    directory1.add_file(file1)
    directory1.add_file(file2)
    directory2.add_file(file3)
    root = Directory('root')
    root.add_file(directory1)
    root.add_file(directory2)
    print(root.show())
