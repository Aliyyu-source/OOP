# menu.py

from iot_device import IoTDevice, TemperatureSensor, HumiditySensor, MotionSensor
from file_handler import FileHandler
from encryptor import Encryptor

class Menu:
    def __init__(self) -> None:
        self.devices = []
        self.file_handler = FileHandler("iot_data.csv")
        self.encrypted_rows = []
        return None

    def run(self) -> None:
        print("Program starting.")
        running = True
        while running:
            choice = self.ask_choice()
            if choice == 1:
                self.add_device()
            elif choice == 2:
                self.serialize_data()
            elif choice == 3:
                self.deserialize_data()
            elif choice == 4:
                self.encrypt_data()
            elif choice == 5:
                self.decrypt_data()
            elif choice == 0:
                running = False
            else:
                print("Invalid choice. Please try again.")
        print("Program ending.")
        return None

    def ask_choice(self) -> int:
        print("\nOptions:")
        print("1 - Add IoT Device")
        print("2 - Serialize Data")
        print("3 - Deserialize Data")
        print("4 - Encrypt Data")
        print("5 - Decrypt Data")
        print("0 - Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1
        return choice

    def add_device(self) -> None:
        print("\nDevice types:")
        print("1 - TemperatureSensor")
        print("2 - HumiditySensor")
        print("3 - MotionSensor")
        try:
            type_choice = int(input("Choose device type: "))
        except ValueError:
            print("Invalid input.")
            return None

        device_id = input("Enter device ID: ")
        location = input("Enter location: ")
        data = input("Enter data value: ")

        if type_choice == 1:
            device = TemperatureSensor(device_id, location, data)
        elif type_choice == 2:
            device = HumiditySensor(device_id, location, data)
        elif type_choice == 3:
            device = MotionSensor(device_id, location, data)
        else:
            print("Invalid device type.")
            return None

        self.devices.append(device)
        print("Device added.")
        return None

    def serialize_data(self) -> None:
        if len(self.devices) == 0:
            print("No devices to serialize.")
            return None
        rows = []
        for device in self.devices:
            row = device.serialize()
            rows.append(row)
        self.file_handler.write(rows)
        print("Data serialized and saved to iot_data.csv.")
        return None

    def deserialize_data(self) -> None:
        rows = self.file_handler.read()
        if len(rows) == 0:
            print("No data found in file.")
            return None
        self.devices = []
        print("\n#### Deserialized Devices ####")
        for row in rows:
            device = IoTDevice.deserialize(row)
            self.devices.append(device)
            device.display()
        print("#### Deserialized Devices ####")
        return None

    def encrypt_data(self) -> None:
        rows = self.file_handler.read()
        if len(rows) == 0:
            print("No data to encrypt. Serialize first.")
            return None
        self.encrypted_rows = []
        for row in rows:
            encrypted = Encryptor.encrypt(row)
            self.encrypted_rows.append(encrypted)
        self.file_handler.write(self.encrypted_rows)
        print("Data encrypted and saved.")
        return None

    def decrypt_data(self) -> None:
        rows = self.file_handler.read()
        if len(rows) == 0:
            print("No data to decrypt.")
            return None
        decrypted_rows = []
        print("\n#### Decrypted Data ####")
        for row in rows:
            decrypted = Encryptor.decrypt(row)
            decrypted_rows.append(decrypted)
            print(decrypted)
        self.file_handler.write(decrypted_rows)
        print("#### Decrypted Data ####")
        return None
