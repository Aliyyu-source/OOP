from score_tracker import ScoreTracker

def main():
    tracker = ScoreTracker()

    print("Program starting.")

    while True:
        print("1 - Add points")
        print("2 - Show score")
        print("3 - Reset score")
        print("0 - Exit program")

        choice = input("Your choice: ")

        if choice == "1":
            try:
                amount = int(input("Enter points to add: "))
                if amount > 0:
                    tracker.addPoints(amount)
                    print(f"Added {amount} points.")
                else:
                    print("Points must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            print(f"Current score: {tracker.getPoints()}")

        elif choice == "3":
            prev = tracker.reset()
            print(f"Score reset. Previous score was {prev}.")

        elif choice == "0":
            print("Program ending.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
