def gen_range(n):
    print("Entering")
    value = 0
    while value < n:
        yield value
        value += 1


def main():
    g = gen_range(10)
    for n in g:
        if n == 7:
            break
    print(next(g))


if __name__ == '__main__':
    main()
