from collections import defaultdict

def main():
    ice_cream = defaultdict(lambda: 'Vanilla')
    ice_cream['Bob'] = 'Chunky Bits'
    ice_cream['Anna'] = 'Good Butter'
    print(ice_cream['Bob'])
    print(ice_cream['Joe'])

    numbers = [1, 2, 1, 4, 2, 6]
    count = defaultdict(int)
    for i in numbers:
        count[i] += 1

    print(count)

if __name__ == '__main__':
    main()
