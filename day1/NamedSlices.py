def main():
    data = "0923847239487239847230840238402384023840238447572305470237"
    price = data[13:16]
    amount = data[21:23]

    print(price)
    print(amount)

    PRICE = slice(13, 16)
    AMOUNT = slice(21, 23)

    price = data[PRICE]
    amount = data[AMOUNT]

    print(price)
    print(amount)

if __name__ == '__main__':
    main()
