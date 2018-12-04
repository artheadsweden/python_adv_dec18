import requests
import time
from functools import wraps


def web_lookup(url, cache={}):
    if url in cache:
        return cache[url]
    page = requests.get(url).text
    cache[url] = page
    return page


def cache(f):
    saved = {}

    @wraps(f)
    def wrapper(url):
        if url in saved:
            return saved[url]
        page = f(url)
        saved[url] = page
        return page
    return wrapper


@cache
def web_lookup2(url):
    return requests.get(url).text


def main():
    start = time.time()
    document = web_lookup2("http://cnn.com")
    end = time.time()
    print(end - start, "seconds")

    start = time.time()
    document = web_lookup2("http://cnn.com")
    end = time.time()
    print(end - start, "seconds")

if __name__ == '__main__':
    main()
