class MyFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print('Entering')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting')
        return self

    def readlines(self):
        return []


# m1 = MyFile('text.txt')

with MyFile('text.txt') as my:  # __enter__
    print('test')
    my.readlines()

# __exit__