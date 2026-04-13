class CoinAcceptor:
    def __init__(self):
        
        self.__amount = 0      # number of coins inserted
        

    def insertCoin(self) -> None:
        """its basically counting the number of coin inserted, every single time a coin is inserted."""
        self.__amount += 1
        

    def getAmount(self) -> int:
        """Gives the number of coins currently in the machine."""
        return self.__amount

    def returnCoins(self) -> int:
        """Returns all coins and resets the machine to zero."""
        returned = self.__amount
        self.__amount = 0
       
        return returned
