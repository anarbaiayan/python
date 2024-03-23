def display_admin_menu():
    print("1. Add manga")
    print("2. Remove manga")
    print("3. List all mangas")
    print("4. Sort manga")
    print("5. Filter manga")
    print("6. Read a brief summary")
    print("7. Display users information")
    print("8. Remove user")
    print("9. Exit")


def display_user_menu():
    print("1. List all mangas")
    print("2. Search for a manga")
    print("3. Buy a manga")
    print("4. Sort manga")
    print("5. Filter manga")
    print("6. Read a brief summary")
    print("7. Exit")


def get_manga_details():
    title = input("Enter the manga title: ")
    author = input("Enter the author's name: ")
    price = float(input("Enter the price: "))
    genre = input("Enter the genre: ")
    age_rating = input("Enter the age rating: ")
    release_date = int(input("Enter the release date: "))
    summary = input("Enter the summary of the manga:")
    return title, author, price, genre, age_rating, release_date, summary
