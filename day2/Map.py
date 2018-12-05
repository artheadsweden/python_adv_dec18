def combine(size, color, garment):
    return f"{color} {garment} in size {size}"

def main():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x + 2, numbers))
    print(result)

    result = [x + 2 for x in numbers]

    sizes = ['small', 'medium', 'large']
    colors = ['red', 'blue', 'brown']
    garments = ['hat', 'shirt', 'pants']

    items = list(map(combine, sizes, colors, garments))

    for item in items:
        print(item)

    items = [combine(s, c, g) for s, c, g in zip(sizes, colors, garments)]

    for item in items:
        print(item)


if __name__ == '__main__':
    main()
