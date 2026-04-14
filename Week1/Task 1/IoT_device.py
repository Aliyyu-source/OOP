# iot_device.py

from dataclasses import dataclass

@dataclass
class IoTDevice:
    SEPARATOR = ","

    deviceId: str
    location: str
    data: str
    device_type: str

    @staticmethod
    def deserialize(row: str) -> 'IoTDevice':
        columns = row.split(IoTDevice.SEPARATOR)
        device_type = columns[0]

        if device_type == "TemperatureSensor":
            return TemperatureSensor(columns[1], columns[2], columns[3], columns[4])
        elif device_type == "HumiditySensor":
            return HumiditySensor(columns[1], columns[2], columns[3], columns[4])
        elif device_type == "MotionSensor":
            return MotionSensor(columns[1], columns[2], columns[3], columns[4])
        else:
            return IoTDevice(columns[1], columns[2], columns[3], device_type)

    def serialize(self) -> str:
        columns = []
        columns.append(self.device_type)
        columns.append(self.deviceId)
        columns.append(self.location)
        columns.append(self.data)
        columns.append(self.get_unit())
        row = self.SEPARATOR.join(columns)
        return row

    def get_unit(self) -> str:
        return ""

    def display(self) -> None:
        print(f"[{self.device_type}] ID: {self.deviceId} | Location: {self.location} | Data: {self.data} {self.get_unit()}")
        return None


@dataclass
class TemperatureSensor(IoTDevice):
    unit: str = "C"

    def __init__(self, deviceId: str, location: str, data: str, unit: str = "C") -> None:
        self.deviceId = deviceId
        self.location = location
        self.data = data
        self.unit = unit
        self.device_type = "TemperatureSensor"

    def get_unit(self) -> str:
        return self.unit


@dataclass
class HumiditySensor(IoTDevice):
    unit: str = "%"

    def __init__(self, deviceId: str, location: str, data: str, unit: str = "%") -> None:
        self.deviceId = deviceId
        self.location = location
        self.data = data
        self.unit = unit
        self.device_type = "HumiditySensor"

    def get_unit(self) -> str:
        return self.unit


@dataclass
class MotionSensor(IoTDevice):
    unit: str = "detected"

    def __init__(self, deviceId: str, location: str, data: str, unit: str = "detected") -> None:
        self.deviceId = deviceId
        self.location = location
        self.data = data
        self.unit = unit
        self.device_type = "MotionSensor"

    def get_unit(self) -> str:
        return self.unit
