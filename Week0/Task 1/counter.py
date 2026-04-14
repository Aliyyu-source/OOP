class Counter:
    def __init__(self):
        self.__count = 0  # it starts from 0

    def addCount(self):
        self.__count += 1  # add 1 to count

    def getCount(self):
        return self.__count  # return current count

    def zeroCount(self):
        self.__count = 0  # remove all count and set to 0