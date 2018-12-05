def genco():
    data = "Hi there"
    while True:
        f = yield
        f(data)


def main():
    gc = genco()
    next(gc)
    gc.send(lambda value: print(value))


if __name__ == '__main__':
    main()
