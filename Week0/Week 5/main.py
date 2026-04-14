from score_tracker import ScoreTracker

def show_menu():
    print("1 - Add points")
    print("2 - Show score")
    print("3 - Reset score")
    print("0 - Exit program")

def main():
    tracker = ScoreTracker()
    print("Program starting.")

    while True:
        show_menu()
        choice = input("Your choice: ")

        if choice == "1":
            try:
                points = int(input("Enter points to add: "))
                tracker.addPoints(points)
                if points > 0:
                    print(f"Added {points} points.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            current_points = tracker.getPoints()
            print(f"Current score: {current_points}")

        elif choice == "3":
            previous = tracker.reset()
            print(f"Score reset. Previous score was {previous}.")

        elif choice == "0":
            print("Program ending.")
            break

        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")

if __name__ == "__main__":
    main()
``
