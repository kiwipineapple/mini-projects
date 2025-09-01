import math


def add(num1, num2):
    print(num1 + num2)


def min(num1, num2):
    print(num1 - num2)


def mul(num1, num2):
    print(num1 * num2)


def div(num1, num2):
    print(num1 / num2)


def wurzel(num):
    print(math.sqrt(num))


def ceil(num):
    print(math.ceil(num))


def betrag(num):
    print(abs(num))


def main():
    x = input('What do you want calculate? ').lower().split()
    # try x:
    #     continue
    # except:
    #     print('input empty!')

    if '+' in x:
        num1 = int(x[0])
        num2 = int(x[2])
        add(num1, num2)
    elif '-' in x:
        num1 = int(x[0])
        num2 = int(x[2])
        min(num1, num2)
    elif '*' in x:
        num1 = int(x[0])
        num2 = int(x[2])
        mul(num1, num2)
    elif '/' in x:
        num1 = int(x[0])
        num2 = int(x[2])
        div(num1, num2)
    elif 'wurzel' in x:
        for s in x:
            if s.isdigit():
                num = int(s)
                wurzel(num)
    elif 'ceil' in x:
        for s in x:
            if s.isdigit():
                num = int(s)
                ceil(num)

    elif 'betrag' in x:
        for s in x:
            if s.isdigit():
                num = int(s)
                betrag(num)


main()
