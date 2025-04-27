def create_user(name: str, balance: float, checking_account: bool) -> object:
    class User:
        def __init__(self, name: str, balance: float, checking_account: bool):
            self.name = name
            self.balance = balance
            self.checking_account = checking_account
        
        def withdraw(self, v: float) -> str:
            if v > self.balance:
                raise ValueError()
            self.balance -= v
            return "{} has {}.".format(self.name, int(self.balance))
        
        def add_cash(self, v: float) -> str:
            self.balance += v
            return "{} has {}.".format(self.name, int(self.balance))
        
        def check(self, other: 'User', v: float) -> str:
            if not other.checking_account:
                raise ValueError()
            s1 = other.withdraw(v)
            s2 = self.add_cash(v)[:-1]
            return "{} and {}".format(s2, s1)
        
        def __str__(self) -> str:
            return "User({}, {}, {})".format(self.name, self.balance, self.checking_account)
    
    return User(name, balance, checking_account)

