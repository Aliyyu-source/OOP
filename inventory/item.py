from dataclasses import dataclass #comes from the stand

@dataclass
class Item:
    SEPARATOR =","
    name: str
    value: float
    category: str
    weight: float

    @staticmethod
    def deserialize(row:str) -> 'Item':
        columns = row.split(Item.SEPARATOR)  #Comma separator
        item = Item(
            columns[0], #name
            columns[1], #value
            columns[2], #category
            columns[3], #weight
        )
        return item
    
    def display_price(self):
        print(f"{self.name}  costs {self.value}  $.")
        return None
        