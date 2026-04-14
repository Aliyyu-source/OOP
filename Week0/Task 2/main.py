"""
main.py

Interactive menu-driven program that uses TemperatureConverter.
Output text is designed to match the user's expected transcript exactly.
"""

from temperature__converter import TemperatureConverter

def print_menu() -> None:
    print("Options:")
    print("1) Set temperature")
    print("2) Convert to Celsius")
    print("3) Convert to Fahrenheit")
    print("4) Convert to Kelvin")
    print("0) Exit program")

def main() -> None:
    print("Program starting.")
    print("Initializing temperature converter...")
    converter = TemperatureConverter()
    print("Temperature converter initialized.")
    while True:
        
        print_menu()
        choice = input("Choice: ").strip()
        if choice == '1':
            try:
                temp_str = input("Enter temperature: ").strip()
                temp_val = float(temp_str)
                converter.setTemperature(temp_val)
                print(f"Temperature set to {converter.toCelsius():.1f}")
            except ValueError:
                # If user enters a non-numeric value, ignore and re-show the menu
                # The spec doesn't define error text, so we keep output minimal.
                pass
        elif choice == '2':
            print(f"Temperature in Celsius: {converter.toCelsius():.1f}")
        elif choice == '3':
            print(f"Temperature in Fahrenheit: {converter.toFahrenheit():.1f}")
        elif choice == '4':
            print(f"Temperature in Kelvin: {converter.toKelvin():.2f}")
        elif choice == '0':
            print("Program ending.")
            break
        else:
            # Unrecognized input: simply re-show menu without extra text
            continue

if __name__ == "__main__":
    main()