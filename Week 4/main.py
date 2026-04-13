from coin_acceptor import CoinAcceptor

def main() -> None:   #This creates a function called main that returns nothing (None)
    
    machine = CoinAcceptor()

    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    print()

    while True:
        user_input = input("Insert coin(0 return, -1 exit): ")
        value = float(user_input)   

        if value == -1:
            print("Exiting program.")
            break

        elif value == 0:
            print("Returning coins...")
            returned_amount, returned_value = machine.returnCoins()
            print(f"{returned_amount} coins with {returned_value}€ value returned.")
            print(f"Inserted coins = {machine.getAmount()}, value = {machine.getValue()}€")
            print()

        elif value > 0:
            print("Inserting...")
            machine.insertCoin(value)
            print(f"Inserted coins = {machine.getAmount()}, value = {machine.getValue()}€")
            print()

        else:
            print("Invalid coin value.")
            print()

    print()
    print("Program ending.")


if __name__ == "__main__":
    main() 
