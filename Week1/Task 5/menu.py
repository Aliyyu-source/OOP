# menu.py

from entity import Player, NPC, Object, interact_all

class Menu:
    def __init__(self) -> None:
        self.entities = []
        return None

    def run(self) -> None:
        print("Program starting.")
        running = True
        while running:
            choice = self.ask_choice()
            if choice == 1:
                self.add_entity()
            elif choice == 2:
                self.interact_with_entities()
            elif choice == 0:
                running = False
            else:
                print("Invalid choice. Please try again.")
        print("Program ending.")
        return None

    def ask_choice(self) -> int:
        print("\nOptions:")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("0 - Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1
        return choice

    def add_entity(self) -> None:
        print("\nEntity types:")
        print("1 - Player")
        print("2 - NPC")
        print("3 - Object")
        try:
            type_choice = int(input("Choose entity type: "))
        except ValueError:
            print("Invalid input.")
            return None

        name = input("Enter entity name: ")
        position = input("Enter position: ")

        if type_choice == 1:
            try:
                level = int(input("Enter player level: "))
            except ValueError:
                level = 1
            entity = Player(name, position, level)
        elif type_choice == 2:
            dialogue = input("Enter NPC dialogue: ")
            entity = NPC(name, position, dialogue)
        elif type_choice == 3:
            item_type = input("Enter object type (e.g. chest, door, key): ")
            entity = Object(name, position, item_type)
        else:
            print("Invalid entity type.")
            return None

        self.entities.append(entity)
        print(f"Entity '{entity}' added.")
        return None

    def interact_with_entities(self) -> None:
        if len(self.entities) == 0:
            print("No entities added yet.")
            return None
        interact_all(self.entities)
        return None
