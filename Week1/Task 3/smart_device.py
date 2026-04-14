# smart_device.py

class SmartDevice:
    deviceName: str
    status: str

    def __init__(self, deviceName: str, status: str = "off") -> None:
        self.deviceName = deviceName
        self.status = status
        return None

    def __str__(self) -> str:
        return f"{self.deviceName} (status: {self.status})"

    def operate(self) -> None:
        print(f"{self.deviceName} is operating.")
        return None


class SmartLight(SmartDevice):
    brightness: int

    def __init__(self, deviceName: str, brightness: int = 50) -> None:
        super().__init__(deviceName)
        self.brightness = brightness
        return None

    def operate(self) -> None:
        if self.status == "off":
            self.status = "on"
            print(f"{self.deviceName} turned ON at {self.brightness}% brightness.")
        else:
            self.status = "off"
            print(f"{self.deviceName} turned OFF.")
        return None


class SmartThermostat(SmartDevice):
    temperature: float

    def __init__(self, deviceName: str, temperature: float = 20.0) -> None:
        super().__init__(deviceName)
        self.temperature = temperature
        return None

    def operate(self) -> None:
        if self.status == "off":
            self.status = "on"
            print(f"{self.deviceName} turned ON. Setting temperature to {self.temperature}°C.")
        else:
            self.status = "off"
            print(f"{self.deviceName} turned OFF.")
        return None


class SmartLock(SmartDevice):
    is_locked: bool

    def __init__(self, deviceName: str) -> None:
        super().__init__(deviceName)
        self.is_locked = True
        self.status = "locked"
        return None

    def operate(self) -> None:
        if self.is_locked:
            self.is_locked = False
            self.status = "unlocked"
            print(f"{self.deviceName} is now UNLOCKED.")
        else:
            self.is_locked = True
            self.status = "locked"
            print(f"{self.deviceName} is now LOCKED.")
        return None


def operate_all_devices(devices: list) -> None:
    print("\n#### Operating all devices ####")
    for device in devices:
        device.operate()
    print("#### Done ####")
    return None
