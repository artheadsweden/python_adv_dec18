def s(a, b):
    return a + b


def d(a, b):
    return a - b


def p(a, b):
    return a * b


def q(a, b):
    return a / b


def main():
    calc = {
        "sum": s,
        "diff": d,
        "product": p,
        "quotient": q
    }

    print(calc['sum'](2,3))
    print(calc['diff'](2,3))
    print(calc['product'](2,3))
    print(calc['quotient'](2,3))

    for k, f in calc.items():
        print(k, '-', f(2, 3))

    calc2 = {
        "sum": lambda a, b: a + b,
        "diff":  lambda a, b: a - b,
        "product": lambda a, b: a * b,
        "quotient": lambda a, b: a / b
    }

    for k, f in calc2.items():
        print(k, '-', f(2, 3))

    test_dict = {
        s: "Sub",
        d: "Diff"
    }

    for f, v in test_dict.items():
        print(v, f(3, 4))


if __name__ == '__main__':
    main()
