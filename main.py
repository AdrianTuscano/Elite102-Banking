import mysql.connector
import random


connection = mysql.connector.connect(user = "root", database = "example", password = "password")



def create_account():
    user = input("What do you want your username to be?")
    passcode = input("What do you want your passcode to be?")
    
    # Generating unique ID

    cursor = connection.cursor()

    testQuery = ("SELECT ID FROM bank_system")

    cursor.execute(testQuery)
    activeids = []
    for item in cursor:
        activeids.append(item[0])

    while True:
        id = random.randint(1, 9999)
        if id not in activeids:
            break
    
    # Adding Account

    cursor = connection.cursor()

    addData = (f"INSERT INTO bank_system (ID, USER, PIN, BAL) VALUES ( '{id}', '{user}', '{passcode}', '0.0' )")

    cursor.execute(addData)

    connection.commit()
    print(f"Account Created! You can now log in. Your ID is {id}")

def log_in():
    inputtedid = int(input("What is your ID? 4-digit number:"))

    cursor = connection.cursor()

    testQuery = ("SELECT ID FROM bank_system")

    cursor.execute(testQuery)
    activeids = []
    for item in cursor:
        activeids.append(item[0])
    if inputtedid in activeids:
        print("ID found")
        inputtedpin = input("What is your pin? String:")
        # Getting pin of relative ID
        cursor = connection.cursor()
        testQuery = (f"SELECT PIN FROM bank_system WHERE ID = '{inputtedid}'")
        cursor.execute(testQuery) #weird formatting when extracting data from sql
        pin = cursor.fetchall()[0][0]

        if str(pin) == str(inputtedpin):
            interface(inputtedid)
        else:
            print("Wrong PIN")
    else:
         print("No ID found")

def interface(loggedinID):
    print("Welcome to your dashboard!")
    ID = loggedinID
    while True:
    # UI Code
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Log Out")

        choice = input("Enter your choice: ")
        # Logic for the multiple choice input
        if choice == "1":
            # Check BAL
            print("Checking current balance...")
            cursor = connection.cursor()
            testQuery = (f"SELECT BAL FROM bank_system WHERE ID = '{ID}'")
            cursor.execute(testQuery)
            balance = cursor.fetchall()[0][0]
            print("$" + str(balance))
        elif choice == "2":
            cursor = connection.cursor()
            testQuery = (f"SELECT BAL FROM bank_system WHERE ID = '{ID}'")
            cursor.execute(testQuery)
            balance = cursor.fetchall()[0][0]

            depositamount = float(input("How much would you like to Deposit?"))
            newbal = balance + depositamount
            cursor = connection.cursor()
            testQuery = (f"UPDATE bank_system SET BAL = '{str(newbal)}' WHERE ID = '{ID}'")
            cursor.execute(testQuery)
            print(f"Your new balance is {newbal}")
            #  deposit ????? 
        elif choice == "3":
            # Entering withdraw ????
            cursor = connection.cursor()
            testQuery = (f"SELECT BAL FROM bank_system WHERE ID = '{ID}'")
            cursor.execute(testQuery)
            balance = cursor.fetchall()[0][0]

            withdrawamount = float(input("How much would you like to Withdraw?"))
            newbal = balance - withdrawamount
            cursor = connection.cursor()
            testQuery = (f"UPDATE bank_system SET BAL = {str(newbal)} WHERE ID = '{ID}'")
            cursor.execute(testQuery)
            print(f"Your new balance is {newbal}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.") 
# Bank Home Page(create account, log in, admin, quit program)
while True:
    # UI Code
    print("\nOptions:")
    print("1. Create New Account")
    print("2. Log Into Account")
    print("3. Quit")

    choice = input("Enter your choice: ")
    # Logic for the multiple choice input
    if choice == "1":
        # Create new account
        print("Creating New Account...")
        create_account()
    elif choice == "2":
        print("Logging In...")
        log_in()
        # Log into Account

    elif choice == "3":
        print("Goodbye!")
        connection.close
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")