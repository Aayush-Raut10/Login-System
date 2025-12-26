from login import loginSystem

print("=" * 50)
print("\tWelcome to the CLI login system")
print("=" * 50)

print("\n1. Sign-Up \n2. Login\n")

choice = int(input("Enter your choice: "))

if choice == 1:
    pass
elif choice == 2:
    loginSystem()