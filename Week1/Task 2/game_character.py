# game_character.py

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    name: str
    health: int

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        return None

    def __str__(self) -> str:
        return f"{self.name} (HP: {self.health})"

    @abstractmethod
    def attack(self) -> int:
        pass

    @abstractmethod
    def defend(self) -> int:
        pass

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return None


class Warrior(GameCharacter):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=150)
        self.character_class = "Warrior"
        return None

    def attack(self) -> int:
        damage = 25
        print(f"{self.name} swings a sword for {damage} damage!")
        return damage

    def defend(self) -> int:
        shield = 15
        print(f"{self.name} raises a shield, blocking {shield} damage!")
        return shield


class Mage(GameCharacter):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=90)
        self.character_class = "Mage"
        return None

    def attack(self) -> int:
        damage = 40
        print(f"{self.name} casts a fireball for {damage} damage!")
        return damage

    def defend(self) -> int:
        shield = 5
        print(f"{self.name} uses a magic barrier, blocking {shield} damage!")
        return shield


class Archer(GameCharacter):
    def __init__(self, name: str) -> None:
        super().__init__(name, health=110)
        self.character_class = "Archer"
        return None

    def attack(self) -> int:
        damage = 30
        print(f"{self.name} fires an arrow for {damage} damage!")
        return damage

    def defend(self) -> int:
        shield = 10
        print(f"{self.name} dodges, avoiding {shield} damage!")
        return shield


def simulate_battle(characters: list) -> None:
    print("\n#### Battle Start ####")
    if len(characters) < 2:
        print("Need at least 2 characters to battle.")
        return None

    attacker = characters[0]
    defender = characters[1]

    print(f"{attacker} vs {defender}")
    print("")

    damage = attacker.attack()
    blocked = defender.defend()

    actual_damage = damage - blocked
    if actual_damage < 0:
        actual_damage = 0

    defender.take_damage(actual_damage)
    print(f"{defender.name} takes {actual_damage} actual damage.")
    print(f"{defender.name} HP remaining: {defender.health}")

    if not defender.is_alive():
        print(f"{defender.name} has been defeated!")

    print("#### Battle End ####")
    return None
