from task1 import Accounts,InsufficientBalanceError


class SavingsAccounts(Accounts):
    def __init__(self,owner,balance, min_balance=500):
        super().__init__(owner,balance)
        #self.account = Accounts
        self.minBalance = min_balance


    def withdraw(self, amount):
        if self.balance - amount< self.minBalance:
            raise InsufficientBalanceError(
                f"Cannot withdraw {amount}. Minimum balance of {self.min_balance} must be maintained."
            )

        self.balance-=amount
        print(f"Withdrawn {amount}. New Balance {self.balance}")





acc = SavingsAccounts("priya", 1500)
try:
 acc.show()
 acc.deposit(500)
 acc.withdraw(300)
 acc.withdraw(1300)
 acc.show()
except InsufficientBalanceError as e:
    print("error ", e)
finally:
     print("Transaction completed.")