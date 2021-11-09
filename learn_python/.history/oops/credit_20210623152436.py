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
    ”””Return current credit limit.”””
    return self.limit

    def get_balance(self):
        return self.balance
