my_balance = 0


def withdrawl():
    global my_balance
    withdraw = input("Enter how much money you want to withdraw from your bank? ")
    if withdraw.isdigit():
        withdraw = int(withdraw)
        if withdraw <= 0:
            print("You can't withdraw negative or zero amount of money.")
            withdrawl()
        else:
            my_balance -= withdraw
            print(f"You have withdrawl {withdraw} from your bank.")
            print(f"Your current balance is {my_balance}.")
    else:
        print("Invalid input")
        withdrawl()
    
def deposit():
    global my_balance
    deposit_money = input("Enter how much money you want to deposit in your bank? ")
    if deposit_money.isdigit():
        deposit_money = int(deposit_money)
        if deposit_money <= 0:
            print("You can't deposit negative or zero amount of money.")
            deposit()
        else:
            my_balance += deposit_money
            print(f"You have deposited {deposit_money} in your bank.")
            print(f"Your current balance is {my_balance}.")
    else:
        print("Invalid input")
        deposit()

def bank():
    while True:
        options = ["w", "d", "q"]
        print("Press-W for withdrawl money:")
        print("Press-D to deposit money")
        print("Press-Q to Quit")
        user_choice = input("Enter your choice: ").lower()
        
        if user_choice not in options:
            print("\nInvalid choice. Please try again.\n")
            return bank()
        
        if user_choice == 'w':
            withdrawl()

        elif user_choice == 'd':
            deposit()
        
bank()