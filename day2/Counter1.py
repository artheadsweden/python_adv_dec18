from collections import Counter

def main():
    text = "When I was a kid I always wanted a cat but all I got was a gold fish"
    count = Counter(text.split())
    print(count.most_common(3))


if __name__ == '__main__':
    main()
