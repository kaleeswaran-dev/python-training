

class InsufficientBalanceError(Exception):
    pass





class Accounts:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount} New Balance {self.balance}")


    def withdraw(self,amount):
        if amount> self.balance:
            raise InsufficientBalanceError(
                "you don't have enough balance"
            )
        self.balance-= amount
        print(f"withdraw{amount} New Withdraw balance {self.balance}")


    def show(self):
        print(
            f"owner {self.owner}"
        )
        print(
                    f"balance {self.balance}"
                )
        




acc = Accounts("Alice", 1000)


try:
 acc.show()
 acc.deposit(500)
 acc.withdraw(300)
 acc.withdraw(200)
 acc.show()
except InsufficientBalanceError as e:
    print("error ", e)
finally:
     print("Transaction completed.")
