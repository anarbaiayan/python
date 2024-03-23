from user_csv import load_user_data


class User:
    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self.username

class Admin(User):
    pass


def authenticate(username, password, filename='users.csv'):
    user_data = load_user_data(filename)
    if username in user_data and user_data[username][0] == password:
        if username == "Ayan":
            return Admin(username)
        else:
            return User(username)
    return None
