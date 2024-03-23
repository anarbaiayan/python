import json
from catalog import Manga


class Storage:
    def __init__(self, filename, filetype='json'):
        self.filename = filename
        self.filetype = filetype

    def save(self, data):
        if self.filetype == 'json':
            with open(self.filename, 'w') as file:
                json.dump([{'title': manga.get_title(), 'author': manga.get_author(), 'price': manga.get_price(),
                            'genre': manga.get_genre(), 'age_rating': manga.get_age_rating(),
                            'release_date': manga.get_release_date(), 'summary': manga.get_summary()} for manga in data], file, indent=4)

    def load(self):
        try:
            if self.filetype == 'json':
                with open(self.filename, 'r') as file:
                    return [Manga(**manga) for manga in json.load(file)]
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist.")
            return []
        except ValueError:
            print(f"Invalid data format in {self.filename}.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
