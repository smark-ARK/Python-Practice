class CreditCard:

    def init(self, customer, bank, acnt, limit):

        self. customer = customer
        self. bank = bank
        self. account = acnt
        self. limit = limit
        self. balance = 0

    def get_customer(self):
        return self.customer

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.account

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance


if name == __main__:
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings',
                  '56 5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '58 3485 0399 3395 1954', 3500))60 5391 0375 9387 5309, 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 val)
        wallet[2].charge(3 val)

    for c in range(3):
        print(Customer=, wallet[c].get customer())
        print(Bank=, wallet[c].get bank())
        print(Account=, wallet[c].get account())
        print(Limit=, wallet[c].get limit())
        print(Balance=, wallet[c].get balance())
        while wallet[c].get balance() > 100:
        wallet[c].make_payment(100)
        print(New balance=, wallet[c].get balance())
        print()
