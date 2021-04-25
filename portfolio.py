class Portfolio:
    def __init__(self):
        self.holdings = {}

    def purchase(self, symbol, shares):
        self.validate(shares)
        self.holdings[symbol] = self.shares_of(symbol) + shares

    def sell(self, symbol, shares):
        if shares > self.shares_of(symbol):
            raise ValueError('attempt to sell more shares than owned')
        self.holdings[symbol] = self.shares_of(symbol) - shares
        self.remove_symbol_if_empty(symbol)

    def remove_symbol_if_empty(self, symbol):
        if self.shares_of(symbol) == 0:
            self.holdings.pop(symbol, None)

    def validate(self, shares):
        if shares == 0:
            raise ValueError

    def unique_symbol_count(self):
        return len(self.holdings)

    def is_empty(self):
        return self.unique_symbol_count == 0

    def shares_of(self, symbol):
        if symbol not in self.holdings:
            return 0
        return self.holdings[symbol]

    unique_symbol_count = property(unique_symbol_count)
    is_empty = property(is_empty)
