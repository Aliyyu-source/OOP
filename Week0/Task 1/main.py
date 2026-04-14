from counter import Counter

print("Program starting...")
print("Initializing counter...")

counter = Counter()

print("Counter initialized.")

while True:
    print("\nOptions:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("0) Exit program")

    choice = input("Choice: ")

    if choice == "1":
        counter.addCount()
        print("Count increased")

    elif choice == "2":
        print("Current count:", counter.getCount())

    elif choice == "3":
        counter.zeroCount()
        print("Count zeroed")

    elif choice == "0":
        print("\nProgram ending.")
        break

    else:
        print("you have entered wrong input. Please enter 1, 2, 3, or 0.")