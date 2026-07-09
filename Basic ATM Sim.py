balance = 250
pin = 2003
count = 3
attempts = 0
transactions = []
def checkBalance(balance):
    print(f"Your balance is:\n${balance:.2f}")
def deposit(balance, transactions):
    deposit = float(input("How much would you like to deposit? \n"))
    if deposit > 0:
        balance += deposit
        print(f"Your new balance is: ${balance:.2f}")
        transactions.append(f"Deposited ${deposit:.2f}")
    else:
        print("Deposit must be greater than 0!")
    return balance
def withdraw(balance, transactions):
    withdraw = float(input("How much would you like to withdraw? \n"))
    if withdraw >= 1 and withdraw <= balance:
        balance -= withdraw
        print(f"You have withdrawn ${withdraw:.2f}\nYour new balance is:\n${balance:.2f}")
        transactions.append(f"Withdrew ${withdraw:.2f}")
    elif withdraw < 1:
        print("You cannot withdraw less than $1!") 
    else:
        print("You cannot withdraw more than you have!")
    return balance
def transactionHistory(transactions):
    if not transactions:
        print("You have no recent transactions.")
    else:
        for transaction in transactions:
            print(transaction)
menu = ("Welcome to Python ATM \n1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit \n5. Transaction History")
while count > 0:
    attempts = int(input("Enter your pin. \n"))
    if attempts != pin:
        count -= 1
        print("incorrect pin", count, "tries remaining")
        if count == 0:
            print("No more tries remaining, Now closing app.")
            break
    elif attempts == pin:
        print("Welcome!")
        break
if attempts == pin:

    while True:
        print(menu)
        mode = int(input("Choose an option.\n"))
        if mode == 1:
            checkBalance(balance)
        elif mode == 2:
            balance = deposit(balance, transactions)
        elif mode == 3:
            balance = withdraw(balance, transactions)
        elif mode == 4:
            print("Thank you for using Python ATM \nNow Exiting")
            break
        elif mode == 5:
            transactionHistory(transactions)
        else:
            print("Please select an available option!")
