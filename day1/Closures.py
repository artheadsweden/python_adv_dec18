def outer(x):
    def inner(y):
        print(x, y)
    return inner


def func_fact(e):
    def inner(b):
        return b**e
    return inner

def main():
    f = outer(10)
    f(20)
    square = func_fact(2)
    cube = func_fact(3)

    print(square(3))
    print(cube(3))


if __name__ == '__main__':
    main()
