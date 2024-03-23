import json


def getTitle(a):
    return a.get('title')


def getPrice(a):
    return a.get('price')

def getDate(a):
    return a.get('release_date')


def printMangasPrice(sort):
    if sort == "Asc":
        for i in getDataAsc():
            print(i)
    elif sort == "Desc":
        for i in getDataDesc():
            print(i)


def printMangasName(sort):
    if sort == "Asc":
        for i in getDataAscTitle():
            print(i)
    elif sort == "Desc":
        for i in getDataDescTitle():
            print(i)

def printMangasDate(sort):
    if sort == "Asc":
        for i in getDataAscDate():
            print(i)
    elif sort == "Desc":
        for i in getDataDescDate():
            print(i)


def getDataAsc():
    with open('mangas.json', 'r') as file:
        manga = json.load(file)
    dataSort = sorted(manga, key=getPrice)
    return dataSort


def getDataDesc():
    with open('mangas.json', 'r') as file:
        manga = json.load(file)
    dataSort = sorted(manga, key=getPrice, reverse=True)
    return dataSort


def getDataAscTitle():
    with open('mangas.json', 'r') as file:
        manga = json.load(file)
    dataSort = sorted(manga, key=getTitle)
    return dataSort


def getDataDescTitle():
    with open('mangas.json', 'r') as file:
        manga = json.load(file)
    dataSort = sorted(manga, key=getTitle, reverse=True)
    return dataSort

def getDataAscDate():
    with open('mangas.json', 'r') as file:
        manga = json.load(file)
    dataSort = sorted(manga, key=getDate)
    return dataSort


def getDataDescDate():
    with open('mangas.json', 'r') as file:
        manga = json.load(file)
    dataSort = sorted(manga, key=getDate, reverse=True)
    return dataSort