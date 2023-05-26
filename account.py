# Add attributes deposits and withdrawals in the init method which are empty 
# lists by default and another attribute loan_balance which is zero by default.

class Account:
    def __init__(self,deposits,withdrawals,loan_balance):
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0

#  Add a method check_balance which returns the account’s balance
#  in this function, we reduce the loan_balance from the account_balance 
# the Account balance will equal to the sum of deposits -(sum of withdrawals+loan_balance)

    def check_balance(self):
        balance= sum(self.deposits)-(sum(self.withdrawals)+self.loan_balance)
        return (f"Your balance is {balance}")


#  Update the deposit method to append each deposit transaction to the deposits list. 
# Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
       
#   every deposition would be added(append) to the list of deposits.

        
    def Update_deposit(self,amount,sentence):
        
        self.deposits.append({ "amount":{amount},"narration":{sentence}
        })
        
        return (f"your list of deposits was updated to {self.deposits}")
# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
# Every deposit transaction would be added(append) to the list of withdrawals.


    def Update_withdrawal(self,amount,sentence):
        self.withdrawals.append({"amount":{amount}, "narration":{sentence}})
        return (f"your list of withdrawals was updated to {self.withdrawals} ")
  
#    Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500


 def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount

    def borrow_loan(self, amount):
        total_deposits = sum(transaction['amount'] for transaction in self.deposits)
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= total_deposits / 3:
            self.loan_balance += amount
            print("Loan granted!")
        else:
            print("Loan cannot be granted.")

        

       
