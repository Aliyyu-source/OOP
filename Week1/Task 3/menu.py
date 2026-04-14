# menu.py

from smart_device import SmartLight, SmartThermostat, SmartLock, operate_all_devices

class Menu:
    def __init__(self) -> None:
        self.devices = []
        return None

    def run(self) -> None:
        print("Program starting.")
        running = True
        while running:
            choice = self.ask_choice()
            if choice == 1:
                self.add_device()
            elif choice == 2:
                self.operate_devices()
            elif choice == 0:
                running = False
            else:
                print("Invalid choice. Please try again.")
        print("Program ending.")
        return None

    def ask_choice(self) -> int:
        print("\nOptions:")
        print("1 - Add Smart Device")
        print("2 - Operate Devices")
        print("0 - Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1
        return choice

    def add_device(self) -> None:
        print("\nDevice types:")
        print("1 - SmartLight")
        print("2 - SmartThermostat")
        print("3 - SmartLock")
        try:
            type_choice = int(input("Choose device type: "))
        except ValueError:
            print("Invalid input.")
            return None

        name = input("Enter device name: ")

        if type_choice == 1:
            try:
                brightness = int(input("Enter brightness (0-100): "))
            except ValueError:
                brightness = 50
            device = SmartLight(name, brightness)
        elif type_choice == 2:
            try:
                temperature = float(input("Enter temperature (°C): "))
            except ValueError:
                temperature = 20.0
            device = SmartThermostat(name, temperature)
        elif type_choice == 3:
            device = SmartLock(name)
        else:
            print("Invalid device type.")
            return None

        self.devices.append(device)
        print(f"Device '{device}' added.")
        return None

    def operate_devices(self) -> None:
        if len(self.devices) == 0:
            print("No devices added yet.")
            return None
        operate_all_devices(self.devices)
        return None
