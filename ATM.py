class User:
    def __init__(self, fullName, IdCard, LoginId, password, balance):
        self.fullName = fullName
        self.IdCard = IdCard
        self.LoginId = LoginId
        self.password = password
        self.balance = balance

# Register
def register():
    newUser = {}
    userAmount = int(input("How many users do you want to create: "))
    if userAmount < 2:
        print("Can't create less than 2 accounts")
        return False

    for users in range(userAmount):
        print(f"________ Create account {users+1} ________")
        IdCard = int(input("Enter your card ID: "))
        fullName = input("Enter your name: ")
        LoginId = input("Account name: ")
        password = int(input("Password: "))
        balance = int(input("Balance: "))
        user = User(fullName=fullName, IdCard=IdCard, LoginId=LoginId, password=password, balance=balance)
        newUser[LoginId] = user
        print("\n")

    return newUser

# Login after created new user
def login(newUser):
    print("________ Login ________")
    while True:
        LoginId = input("Enter your account ID: ")
        LoginPassword = int(input("Enter your login password: "))
        user = newUser.get(LoginId)
        if user and user.password == LoginPassword:
            print("Login Successfully")
            menu(user, newUser)
            break
        else:
            print("ID or Password Invalid")

# Check user balance
def check(user):
    print(f"Account balance: {user.balance}")

# Withdraw form user account
def withdraw(user):
    print(f"Account balance: {user.balance}")
    withdrawAmount = int(input("Enter amount to withdraw: "))
    if withdrawAmount > user.balance:
        print("Insufficient funds.")
    else:
        user.balance -= withdrawAmount
        print(f"Withdrawal successful. New balance: {user.balance}")

# Deposit to user account
def deposit(user):
    print(f"Account balance: {user.balance}")
    depositAmount = int(input("Enter amount to deposit: "))
    user.balance += depositAmount
    print(f"Deposit successful. New balance: {user.balance}")

# Transfer to another account *Choose target to transfer
def transfer(newUser, user):
    print(f"Account balance: {user.balance}")
    targetLoginId = input("Enter the target account ID: ")
    transferAmount = int(input("Enter amount to transfer: "))
    
    targetUser = newUser.get(targetLoginId)
    
    if not targetUser:
        print("Target account does not exist.")
    elif transferAmount > user.balance:
        print("Insufficient funds.")
    else:
        user.balance -= transferAmount
        targetUser.balance += transferAmount
        print(f"Transfer successful. Your new balance: {user.balance}")
        print(f"Target account new balance: {targetUser.balance}")

# User's menu
def menu(user, newUser):
    while True:
        menuList = int(input("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Logout\nChoose an option: "))
        if menuList == 1:
            check(user)
        elif menuList == 2:
            withdraw(user)
        elif menuList == 3:
            deposit(user)
        elif menuList == 4:
            transfer(newUser, user)
        elif menuList == 5:
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

    # After logging out, allow user to choose another account or exit
    while True:
        choice = input("Do you want to login to another account? (yes/no): ").strip().lower()
        if choice == 'yes':
            login(newUser)
            break
        elif choice == 'no':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    users = register()
    if users:
        login(users)

if __name__ == "__main__":
    main()
