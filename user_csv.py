import csv

def register_user(username, password, filename='users.csv'):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print(f"User {username} registered successfully.")

def load_manga(username, manga_title, filename='users.csv'):
    user_data = load_user_data(filename)
    if username in user_data:
        user_data[username].append(manga_title)
        write_user_data(user_data, filename)
        print(f"Manga '{manga_title}' added to user {username}.")
    else:
        print(f"User {username} not found.")

def load_user_data(filename='users.csv'):
    user_data = {}
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                username = row[0]
                manga_titles = row[1:]
                user_data[username] = manga_titles
    except FileNotFoundError:
        print(f"The file {filename} does not exist. No users loaded.")
    return user_data


def write_user_data(user_data, filename='users.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for username, manga_titles in user_data.items():
            writer.writerow([username] + manga_titles)

def user_exists(username, filename='users.csv'):
    user_data = load_user_data(filename)
    return username in user_data

def print_users_and_mangas(filename='users.csv'):
    user_data = load_user_data(filename)
    for username, manga_titles in user_data.items():
        if username != "Ayan":
            print(f"User: {username}")
            print("Manga Titles:")
        for title in manga_titles[1:]:
            print(f"- {title}")

def remove_user(username, filename='users.csv'):
    user_data = load_user_data(filename)
    if username in user_data:
        del user_data[username]
        write_user_data(user_data, filename)
        print(f"User {username} has been removed.")
    else:
        print(f"User {username} not found.")