class TemperatureConverter:
    def __init__(self):
        self.__temperature = 0.0

    def setTemperature(self, temp: float):
        self.__temperature = temp

    def toCelsius(self):
        return self.__temperature

    def toFahrenheit(self):
        return (self.__temperature * 9/5) + 32

    def toKelvin(self):
        return self.__temperature + 273.15
