from temperature_converter import TemperatureConverter

print("Program starting.")
print("Initializing temperature converter...")
print("Temperature converter initialized.\n")

converter = TemperatureConverter()

while True:
    print("Options:")
    print("1) Set temperature")
    print("2) Convert to Celsius")
    print("3) Convert to Fahrenheit")
    print("4) Convert to Kelvin")
    print("0) Exit program")

    choice = input("Choice: ")

    if choice == "1":
        temp = float(input("Enter temperature: "))
        converter.setTemperature(temp)
        print(f"Temperature set to {converter.toCelsius()}\n")

    elif choice == "2":
        print(f"Temperature in Celsius: {converter.toCelsius()}\n")

    elif choice == "3":
        print(f"Temperature in Fahrenheit: {converter.toFahrenheit()}\n")

    elif choice == "4":
        print(f"Temperature in Kelvin: {converter.toKelvin()}\n")

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid choice.\n")
