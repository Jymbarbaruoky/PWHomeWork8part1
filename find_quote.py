import redis
from redis_lru import RedisLRU

from models import Authors, Quotes

client = redis.StrictRedis(host='localhost', port=6379, username='default', password=None)
cache = RedisLRU(client)


@cache
def search_by_name(name: str):
    autor = Authors.objects(fullname__istartswith=name)
    for a in autor:
        quotes = Quotes.objects(author=a.id)
        for quote in quotes:
            return quote.quote


@cache
def search_by_tag(tag: str):
    quotes = Quotes.objects(tags__istartswith=tag)
    for quote in quotes:
        return quote.quote


def search_by_tags(tags: list):
    quotes = Quotes.objects(tags__in=tags)
    for quote in quotes:
        return quote.quote


def main():
    while True:
        data = (input('Enter comand and value:\n ---> ')).split(':')
        if data[0] == 'name':
            print(search_by_name(data[1].strip()))
        elif data[0] == 'tag':
            print(search_by_tag(data[1].strip().split(',')[0]))
        elif data[0] == 'tags':
            print(search_by_tags(data[1].strip().split(',')))
        elif data[0] == 'exit':
            exit()
        else:
            print('Wrong comand!')


if __name__ == '__main__':
    main()
