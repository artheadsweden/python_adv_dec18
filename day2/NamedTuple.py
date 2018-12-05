from collections import namedtuple

def main():
    Student = namedtuple('Student',['name', 'age', 'email'])

    s = Student("John", '19', 'john@mail.com')
    print(s.name)
    print(s[1])


if __name__ == '__main__':
    main()
