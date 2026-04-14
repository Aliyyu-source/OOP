# crypto_wallet.py

class CryptoWallet:
    def __init__(self, walletId: str) -> None:
        self._walletId = walletId
        self._balance = 0.0
        self._transactions = []
        return None

    def __str__(self) -> str:
        return f"Wallet ID: {self._walletId}"

    def get_wallet_id(self) -> str:
        return self._walletId

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return None
        self._balance += amount
        self._transactions.append(f"Deposit: +{amount}")
        print(f"Deposited {amount}. New balance: {self._balance}")
        return None

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return None
        if amount > self._balance:
            print("Insufficient balance.")
            return None
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -{amount}")
        print(f"Withdrew {amount}. New balance: {self._balance}")
        return None

    def check_balance(self) -> None:
        print(f"Balance for {self._walletId}: {self._balance}")
        return None

    def transaction_history(self) -> None:
        print(f"\n#### Transaction History for {self._walletId} ####")
        if len(self._transactions) == 0:
            print("No transactions yet.")
        for transaction in self._transactions:
            print(transaction)
        print("#### End of History ####")
        return None
