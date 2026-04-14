# menu.py

from crypto_wallet import CryptoWallet

class Menu:
    def __init__(self) -> None:
        self.wallets = []
        return None

    def run(self) -> None:
        print("Program starting.")
        running = True
        while running:
            choice = self.ask_choice()
            if choice == 1:
                self.create_wallet()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.check_balance()
            elif choice == 5:
                self.transaction_history()
            elif choice == 0:
                running = False
            else:
                print("Invalid choice. Please try again.")
        print("Program ending.")
        return None

    def ask_choice(self) -> int:
        print("\nOptions:")
        print("1 - Create Wallet")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Check Balance")
        print("5 - Transaction History")
        print("0 - Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1
        return choice

    def pick_wallet(self) -> CryptoWallet:
        if len(self.wallets) == 0:
            print("No wallets available. Create one first.")
            return None
        print("\nAvailable wallets:")
        for i in range(len(self.wallets)):
            print(f"{i + 1}. {self.wallets[i]}")
        try:
            index = int(input("Choose wallet number: ")) - 1
        except ValueError:
            print("Invalid input.")
            return None
        if index < 0 or index >= len(self.wallets):
            print("Invalid wallet number.")
            return None
        return self.wallets[index]

    def create_wallet(self) -> None:
        wallet_id = input("Enter wallet ID: ")
        wallet = CryptoWallet(wallet_id)
        self.wallets.append(wallet)
        print(f"Wallet '{wallet}' created.")
        return None

    def deposit(self) -> None:
        wallet = self.pick_wallet()
        if wallet is None:
            return None
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount.")
            return None
        wallet.deposit(amount)
        return None

    def withdraw(self) -> None:
        wallet = self.pick_wallet()
        if wallet is None:
            return None
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount.")
            return None
        wallet.withdraw(amount)
        return None

    def check_balance(self) -> None:
        wallet = self.pick_wallet()
        if wallet is None:
            return None
        wallet.check_balance()
        return None

    def transaction_history(self) -> None:
        wallet = self.pick_wallet()
        if wallet is None:
            return None
        wallet.transaction_history()
        return None
