class Manga:
    def __init__(self, title, author, price, genre, age_rating, release_date, summary):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.age_rating = age_rating
        self.release_date = release_date
        self.summary = summary

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price:{self.price}$, Genre: {self.genre}, Age Rating: {self.age_rating}"

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_age_rating(self):
        return self.age_rating

    def set_age_rating(self, age_rating):
        self.age_rating = age_rating

    def get_release_date(self):
        return self.release_date

    def set_release_date(self, release_date):
        self.release_date = release_date

    def get_summary(self):
        return self.summary

    def set_summary(self, summary):
        self.summary = summary


class Catalog:
    def __init__(self):
        self.mangas = []

    def get_mangas(self):
        return self.mangas

    def add_manga(self, manga):
        self.mangas.append(manga)
        print("Manga added to the catalog")

    def remove_manga(self, title):
        for manga in self.mangas:
            if manga.title.lower() == title.lower():
                self.mangas.remove(manga)
                print("Manga removed from the catalog")

    def search_manga(self, search_term):
        return [manga for manga in self.mangas if search_term.lower() in manga.get_title().lower()]

    def filter_genres(self, genres):
        return [manga for manga in self.mangas if genres.lower() in manga.get_genre().lower()]


    def list_mangas(self):
        for manga in self.mangas:
            print(manga)

