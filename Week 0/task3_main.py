from coin_acceptor import CoinAcceptor

machine = CoinAcceptor()

print("Program starting.")

while True:
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")
    choice = input("Your choice: ")
    

    if choice == "1":
        machine.insertCoin()

    elif choice == "2":
        print(f"Currently '{machine.getAmount()}' coins in coin acceptor")

    elif choice == "3":
        returned = machine.returnCoins()
        print(f"Coin acceptor returned '{returned}' coins.")

    elif choice == "0":
        print("Program ending.")
        break

    else:
        print("Invalid choice.")

    print()
