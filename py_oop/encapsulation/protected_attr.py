class Account:
    def __init__(self, title: str, balance: int):
        self.title = title
        self._balance = balance # the underscore indicates this attr is protected
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()

# technically you can access "protected" attr via:
# balance = account._balance, but thats not recommended.
