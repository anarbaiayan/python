import sort
import user_csv
from auth import authenticate, Admin
from catalog import Catalog, Manga
from storage import Storage
from utils import display_admin_menu, display_user_menu, get_manga_details
import filter


def main():
    choice = int(input("1. Register\n2. Login\n"))
    if choice == 1:
        username = input("Username: ")
        password = input("Password: ")
        if len(username) >= 4 and len(password) >= 8:
            if user_csv.user_exists(username):
                print(f"User {username} already exists. Enter another nickname.")
            else:
                user_csv.register_user(username, password)
        elif len(username) < 4:
            print("Username must be at least 4")
        elif len(password) < 8:
            print("Password must be at least 8")
    elif choice == 2:
        username = input("Username: ")
        password = input("Password: ")

        user = authenticate(username, password)
        if user is None:
            print("Authentication failed.")
            return

        is_admin = isinstance(user, Admin)
        catalog = Catalog()
        storage_json = Storage('mangas.json', 'json')

        try:
            catalog.mangas = storage_json.load()
        except FileNotFoundError:
            print("No existing catalog found, starting with an empty catalog.")

        while True:
            if is_admin:
                display_admin_menu()
            else:
                display_user_menu()

            choice = input("Choose an option: ")

            if choice == '1':
                if is_admin:
                    title, author, price, genre, age_rating, release_date, summary = get_manga_details()
                    manga = Manga(title, author, price, genre, age_rating, release_date, summary)
                    catalog.add_manga(manga)
                    storage_json.save(catalog.mangas)
                else:
                    catalog.list_mangas()
            elif choice == '2':
                if is_admin:
                    catalog.list_mangas()
                    title = input("Enter the title of the manga to remove: ")
                    catalog.remove_manga(title)
                    storage_json.save(catalog.mangas)
                else:
                    search_term = input("Enter search term: ")
                    found_mangas = catalog.search_manga(search_term)
                    for manga in found_mangas:
                        print(manga)
            elif choice == '3':
                if is_admin:
                    catalog.list_mangas()
                else:
                    catalog.list_mangas()
                    manga_title = input("Enter the title of the manga to buy: ")
                    found_mangas = catalog.search_manga(manga_title)
                    if found_mangas:
                        user_csv.load_manga(username, manga_title)
                        catalog.remove_manga(manga_title)
                        storage_json.save(catalog.mangas)
                        print(f"You have bought {found_mangas[0]}")
                    else:
                        print("Manga not found.")
            elif choice == '4':
                sort_choice = int(input("1.By price\n2.By title\n3.By release date\n"))
                if sort_choice == 1:
                    sorting = input("Asc/Desc: ")
                    sort.printMangasPrice(sorting)
                elif sort_choice == 2:
                    sorting = input("Asc/Desc: ")
                    sort.printMangasName(sorting)
                elif sort_choice == 3:
                    sorting = input("Asc/Desc: ")
                    sort.printMangasDate(sorting)
            elif choice == '5':
                choice_filter = int(input("1. By price\n2. By genre\n3. By release date\n"))
                if choice_filter == 1:
                    num1 = int(input("From: "))
                    num2 = int(input("To: "))
                    filter.filterPrice(num1, num2)
                elif choice_filter == 2:
                    genre = input("Romance\n Science Fiction\n Drama\n Sports\nSlice of Life\nComedy\nRomantic Comedy\nSupernatural\nAction\nFantasy\nAdventure\nHorror\nPsychological thriller\nShonen\nMecha\nMystery\n")
                    found_mangas = catalog.filter_genres(genre)
                    for manga in found_mangas:
                        print(manga)
                elif choice_filter == 3:
                    num1 = int(input("From: "))
                    num2 = int(input("To: "))
                    filter.filterDate(num1, num2)
            elif choice == '6':
                catalog.list_mangas()
                search_term = input("Enter manga title: ")
                found_mangas = catalog.search_manga(search_term)
                for manga in found_mangas:
                    print(manga.summary)
            elif choice == '7':
                if is_admin:
                    user_csv.print_users_and_mangas()
                else:
                    break
            elif choice == '8':
                user_csv.print_users_and_mangas()
                username = input("Enter username: ")
                user_csv.remove_user(username)
            elif choice == "9":
                break
            else:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
