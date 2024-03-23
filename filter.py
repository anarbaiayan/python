import sort

def filterPrice(num1, num2):
    for manga in sort.getDataAsc():
        price = float(manga.get('price', 0))
        if num1 < num2:
            if num1 < price < num2:
                print(manga)
        else:
            if num2 < price < num1:
                print(manga)


def filterDate(num1, num2):
    for manga in sort.getDataAscDate():
        release_date = float(manga.get('release_date', 0))
        if num1 < num2:
            if num1 < release_date < num2:
                print(manga)
        else:
            if num2 < release_date < num1:
                print(manga)