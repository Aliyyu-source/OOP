class ScoreTracker:
    def __init__(self):
        self.__points = 0   # private property

    def addPoints(self, amount: int) -> None:
        if amount > 0:
            self.__points += amount
        else:
            print("Amount must be a positive integer.")

    def getPoints(self) -> int:
        return self.__points

    def reset(self) -> int:
        previous = self.__points
        self.__points = 0
        return previous
