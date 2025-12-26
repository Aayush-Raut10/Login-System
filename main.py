from login import loginSystem
from signup import signupSystem
import time



while True:

    print("=" * 50)
    print("\tWelcome to the CLI login system")
    print("=" * 50)

    print("\n1. Sign-Up \n2. Login \n3. Exit\n")

    choice = int(input("Enter your choice: "))


    if choice == 1:
        signupSystem()

    elif choice == 2:
        loginSystem()


    elif choice == 3:
        print("Exiting from the system........")
        time.sleep(1)
        break

    else:
        print("Invalid choice.")