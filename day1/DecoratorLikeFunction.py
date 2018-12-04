def outer(f):
    def inner(n):
        return ">>>>> " + f(n) + " <<<<<<"
    return inner

@outer
def greeting(name):
    return "Hi " + name

def main():
    #global greeting
    #greeting = outer(greeting)
    print(greeting("Anna"))
    print(greeting.__name__)


if __name__ == '__main__':
    main()
