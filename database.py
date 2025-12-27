
def load_users():
    """
    This function loads the users from file into an in-memory dictionary.

    """
    users = {} # dictionary to hold username:password paris
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    username, password = line.split(",")
                    users[username] = password
    except FileNotFoundError:
        pass

    return users

def save_user(username, password):
    """ Adds a new user to the file """

    with open("users.txt", 'a') as file:
        file.write(f"{username},{password}\n") #Append new user

user_database = load_users()