class Wallet:
    currency = ""
    balance = 0

    def add(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("It should be +")

    def spend(self, amount):
        self.balance -= amount

    def print_balance(self):
        print(self.balance, self.currency)

wallet = Wallet()
wallet.balance = 100
wallet.currency = "BGN"
wallet.add(100)
wallet.spend(30)
wallet.print_balance()