class MyCustomList(list):

    def __getitem__(self, item):
        print("getting item")
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if value < 1:
            print("Not adding it")
            return
        super().__setitem__(key, value)

    def append(self, item) -> None:
        if item < 1:
            return
        super().append(item)


class AppException(Exception):

    def __init__(self, msg) -> None:
        super().__init__(msg)


raise AppException("Useless exception")

c = MyCustomList()
print(c)
c.append(9)
c.append(-1)
print(c[0])
c[1] = -6
print(c)
