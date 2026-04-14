# entity.py

class Entity:
    name: str
    position: str

    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        return None

    def __str__(self) -> str:
        return f"{self.name} at {self.position}"

    def interact(self) -> None:
        print(f"{self.name} is interacting.")
        return None


class Player(Entity):
    level: int

    def __init__(self, name: str, position: str, level: int = 1) -> None:
        super().__init__(name, position)
        self.level = level
        return None

    def __str__(self) -> str:
        return f"[Player] {self.name} (Level {self.level}) at {self.position}"

    def interact(self) -> None:
        print(f"Player {self.name} interacts with the environment at {self.position}.")
        return None


class NPC(Entity):
    dialogue: str

    def __init__(self, name: str, position: str, dialogue: str = "Hello!") -> None:
        super().__init__(name, position)
        self.dialogue = dialogue
        return None

    def __str__(self) -> str:
        return f"[NPC] {self.name} at {self.position}"

    def interact(self) -> None:
        print(f"NPC {self.name} says: '{self.dialogue}'")
        return None


class Object(Entity):
    item_type: str

    def __init__(self, name: str, position: str, item_type: str = "item") -> None:
        super().__init__(name, position)
        self.item_type = item_type
        return None

    def __str__(self) -> str:
        return f"[Object] {self.name} ({self.item_type}) at {self.position}"

    def interact(self) -> None:
        print(f"Object {self.name} ({self.item_type}) at {self.position} is examined.")
        return None


def interact_all(entities: list) -> None:
    print("\n#### Interacting with all entities ####")
    for entity in entities:
        entity.interact()
    print("#### Done ####")
    return None
