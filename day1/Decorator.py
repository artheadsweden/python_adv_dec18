from functools import wraps

def signs(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return ">>>>> " + f(*args, **kwargs) + " <<<<<<"
    return wrapper

@signs
def greeting(name):
    return "Hi " + name

@signs
def fancy_greeting(greet, name):
    return greet + " " + name


def main():
    msg1 = greeting("Anna")
    msg2 = fancy_greeting("Yo", "Bob")
    print(msg1)
    print(msg2)


if __name__ == '__main__':
    main()
