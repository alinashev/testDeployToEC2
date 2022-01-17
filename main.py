from Calculate.Calculator import Calculator


def main():
    calculator = Calculator(15)
    arr = calculator.create()
    print(arr)
    for i in arr:
        print(i * 2)


if __name__ == '__main__':
    main()
