from models import Authors, Quotes
import json


def create_autor(path: str):
    with open(path) as f:
        autors = json.load(f)
    for autor in autors:
        a = Authors(fullname=autor.get('fullname'), born_date=autor.get('born_date'), born_location=autor.get('born_location'), description=autor.get('description')).save()


def create_quote(path: str):
    with open(path) as f:
        quotes = json.load(f)
    for quote in quotes:
        autor = Authors.objects(fullname=quote.get('author'))
        for a in autor:
            q = Quotes(tags=quote.get('tags'), author=a.id, quote=quote.get('quote')).save()


def create():
    model = input('Select model:\n   1 - Autor,\n   2 - Quote.\n ---> ')
    path = input('Enter path to json file\n ---> ')
    if model == '1':
        create_autor(path)
        print('File loaded to db')
    elif model == '2':
        create_quote(path)
        print('File loaded to db')
    else:
        print('Wrong select of model!')


if __name__ == '__main__':
    create()
