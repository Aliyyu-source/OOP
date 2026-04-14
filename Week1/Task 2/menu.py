# menu.py

from game_character import Warrior, Mage, Archer, simulate_battle

class Menu:
    def __init__(self) -> None:
        self.characters = []
        return None

    def run(self) -> None:
        print("Program starting.")
        running = True
        while running:
            choice = self.ask_choice()
            if choice == 1:
                self.create_character()
            elif choice == 2:
                self.start_battle()
            elif choice == 0:
                running = False
            else:
                print("Invalid choice. Please try again.")
        print("Program ending.")
        return None

    def ask_choice(self) -> int:
        print("\nOptions:")
        print("1 - Create Character")
        print("2 - Simulate Battle")
        print("0 - Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1
        return choice

    def create_character(self) -> None:
        print("\nCharacter classes:")
        print("1 - Warrior")
        print("2 - Mage")
        print("3 - Archer")
        try:
            class_choice = int(input("Choose class: "))
        except ValueError:
            print("Invalid input.")
            return None

        name = input("Enter character name: ")

        if class_choice == 1:
            character = Warrior(name)
        elif class_choice == 2:
            character = Mage(name)
        elif class_choice == 3:
            character = Archer(name)
        else:
            print("Invalid class choice.")
            return None

        self.characters.append(character)
        print(f"Character {character} created.")
        return None

    def start_battle(self) -> None:
        if len(self.characters) < 2:
            print("Need at least 2 characters. Create more characters first.")
            return None
        print("\nAvailable characters:")
        for i in range(len(self.characters)):
            print(f"{i + 1}. {self.characters[i]}")
        simulate_battle(self.characters)
        return None
