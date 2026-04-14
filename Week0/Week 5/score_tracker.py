class ScoreTracker:
    def __init__(self):
        # Private property to store points
        self.__points = 0

    def addPoints(self, amount: int) -> None:
        if amount > 0:
            self.__points += amount
        else:
            print("Points to add must be a positive integer.")

    def getPoints(self) -> int:
        return self.__points

    def reset(self) -> int:
        previous_points = self.__points
        self.__points = 0
        return previous_points
