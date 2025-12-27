import database 

def signupSystem():
    
    while True:
        usr_name = input("Enter Username: ").strip()

        if usr_name in database.user_database:
            print("This username already exits. Try another.")
            continue

        password = input("Enter Password: ").strip()
        confirm_password = input("Confirm Password: ").strip()

        if password != confirm_password:
            print("Password and confirm password do not match.")
            continue

        database.user_database[usr_name] = password
        database.save_user(usr_name,password)
        print("Sign-up completed! You can now log-in.\n")
        break

