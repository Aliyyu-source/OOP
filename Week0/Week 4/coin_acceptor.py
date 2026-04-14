class CoinAcceptor:
    def __init__(self) -> None:
        self.__amount = 0 # it starts with 0 coins
        self.__value = 0.0 # it starts with 0.0 value

    def insertCoin(self, coin_value: float) -> None:
        self.__amount += 1 # every time a coin is inserted, the amount increases by 1
        self.__value += coin_value # every time a coin is inserted, the value increases by the value of the coin

    def getAmount(self) -> int:    # count the amount of coins inserted every time
        return self.__amount   

    def getValue(self) -> float: # count the value of coins inserted every time
        return self.__value

    def returnCoins(self) -> tuple[int, float]:  # return the amount and value of coins inserted, and reset the amount and value to 0
        returned_amount = self.__amount
        returned_value = self.__value
        self.__amount = 0
        self.__value = 0.0
        return returned_amount, returned_value
