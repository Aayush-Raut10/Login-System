import database

def loginSystem():


    while True:

        user_name = input("Enter username: ")

        if user_name in database.user_database:

            att = 0
            max_att = 3
            
            while (att < 3):

                password = (input("Enter password: "))

                if password == database.user_database[user_name]:
                    print("Login successful.")
                    break
                else:
                    print("Incorrect password.")
                    att += 1

            else:
                print("Account locked due to too many failed attempts.")

        else:
            print("Username not found!")
        
        try_anotheruser = input("Try another username ? (yes / no ): ").lower()
        if try_anotheruser != "yes":
            print("Terminating the login process.....")
            break

