def gen():
    my_numbers = [1, 2, 3, 4, 5]
    for value in my_numbers:
        yield value**2

def main():
    my_numbers = [1, 2, 3, 4, 5]

    g = (value**2 for value in my_numbers)
    for n in g:
        print(n)


if __name__ == '__main__':
    main()
