from models import Authors, Quotes


def search():
    while True:
        data = (input('Enter comand and value:\n ---> ')).split(':')
        if data[0] == 'name':
            autor = Authors.objects(fullname__istartswith=data[1].strip())
            for a in autor:
                quotes = Quotes.objects(author=a.id)
                for quote in quotes:
                    print(quote.quote)
        elif data[0] == 'tag':
            quotes = Quotes.objects(tags__istartswith=data[1].strip().split(',')[0])
            for quote in quotes:
                print(quote.quote)
        elif data[0] == 'tags':
            quotes = Quotes.objects(tags__in=data[1].strip().split(','))
            for quote in quotes:
                print(quote.quote)
        elif data[0] == 'exit':
            exit()
        else:
            print('Wrong comand!')



if __name__ == '__main__':
    search()


