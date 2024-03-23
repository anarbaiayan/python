import csv
import json
import os


# Authentication
def Authentication():
    print("Login")
    print("Exit")
    choice = input("Input your choice: ")

    valid_user = "Ayan Anarbay"
    valid_password = "******"
    # Cheking for valid password and username
    if choice == "Login":
        username = input("Username: ")
        password = input("Password: ")
        if valid_user == username and valid_password == password:
            print("Successfully logged in")
            return True
        else:
            print("Invalid")
            return False
    else:
        exit()


# Creating folders to store data
def directories():
    os.makedirs("BookstoreData/Books", exist_ok=True)
    os.makedirs("BookstoreData/Customers", exist_ok=True)


# Creating csv file for books
def add_books_csv():
    header = ["Title", "Author", "Publication Year", "Price", "Amount"]
    data = [
        ("Naruto", "Kishimoto Masashi", 1999, 60.0, 30),
        ("Fairy Tail", "Hiro Mashima", 2006, 50.0, 10),
    ]

    with open("BookstoreData/Books/Books.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


# Creating csv file for customers
def add_customers_csv():
    header = ["Name", "Email", "Order History"]
    data = [
        ("Ayan", "anarbajaan1@gmail.com", ""),
        ("admin", "admin@gmail.com", "")
    ]

    with open("BookstoreData/Customers/Customers.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


# Creating reader
def convert_books():
    with open("BookstoreData/Books/Books.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        books_data = [tuple(row) for row in reader]
    return books_data


# Creating dictionary for books
def create_books_dictionary(books_data):
    books_dict = {}
    for book in books_data:
        title = book[0]
        books_dict[title] = {"Author": book[1], "Publication Year": book[2], "Price": book[3], "Amount": book[4]}
    return books_dict


# Creating dictionary for customers
def create_customers_dictionary():
    customers_dict = {}
    with open("BookstoreData/Customers/Customers.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[0]
            customers_dict[name] = {"Email": row[1], "Order History": row[2]}
    return customers_dict


# Writing data to file
def write_data_to_file(file_path, data):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        if isinstance(data, dict):
            writer.writerow(data.keys())
            writer.writerows(data.values())
        elif isinstance(data, list):
            writer.writerows(data)


# Creating json and convertind books to it
def books_to_json(books_data):
    with open("BookstoreData/inventory.json", mode="w", newline="") as file:
        json.dump(books_data, file)


# Creating program that cheks for errors
def read_json():
    try:
        with open("BookstoreData/inventory.json", mode="r", newline="") as file:
            inventory_data = json.load(file)
        return inventory_data
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError as error:
        print(f"Error decoding json: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


# Creating a program that order your book
def place_order(books_dict, customers_dict):
    book_title = input("Enter book title: ")

    if book_title in books_dict:
        customers_name = input("Enter your name: ")
        if customers_name in customers_dict:
            order_history = customers_dict[customers_name]["Order History"]
            order_history += f", {book_title}"
            customers_dict[customers_name]["Order History"] = order_history
            write_data_to_file("BookstoreData/Customers/customers.csv", [customers_dict[customers_name]])
            books_to_json(books_dict)
            print(f"Order placed successfully: {book_title}")
        else:
            print("Customer not found")
    else:
        print("Book not found")


# Here it all used
if Authentication():
    directories()
    add_books_csv()
    add_customers_csv()
    books_data = convert_books()
    books_to_json(books_data)
    inventory_data = read_json()
    books_dict = create_books_dictionary(books_data)
    customers_dict = create_customers_dictionary()

    while True:
        print("\n1. Display books\n2. Place order\n3. Display inventory\n4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            for row in books_data:
                print(f"Title: {row[0]}, Author: {row[1]}, Publication Year: {row[2]}, Price: {row[3]}, Amount: {row[4]}")
        elif choice == "2":
            place_order(books_dict, customers_dict)
        elif choice == "3":
            for book_title, book_details in books_dict.items():
                stock = book_details.get("Amount")
                print(f"Book {book_title}, Stock: {stock}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again")