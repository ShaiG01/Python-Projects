numberList = []
total = None  # Start with None so we know when total hasn't been set

def advancedCalc():
    global total
    try:
        operation = input('Operation (+, -, *, /): ')
        numbers = list(map(int, numberList))  # Convert all to integers

        def add(*args):
            global total
            for arg in args:
                total += arg
            return total

        def subtract(*args):
            global total
            for arg in args:
                total -= arg
            return total

        def multiply(*args):
            global total
            for arg in args:
                total *= arg
            return total

        def divide(*args):
            global total
            for arg in args:
                if arg == 0:
                    print("Error: Division by zero")
                    return
                total /= arg
            return total

        if not numbers:
            print("No numbers entered.")
            return

        if total is None:
            # Initialize total with first number for subtract, divide, multiply
            if operation in ['-', '/', '*']:
                total = numbers[0]
                numbers = numbers[1:]
            else:
                total = 0  # For addition

        if operation == "+":
            add(*numbers)

        elif operation == "-":
            subtract(*numbers)

        elif operation == "*":
            multiply(*numbers)

        elif operation == "/":
            divide(*numbers)

        else:
            print("Invalid operation")

        print(f"Total: {total}")
        numberList.clear()

    except ValueError:
        numberList.clear()
        print("Invalid input. Numbers must be integers.")
    except ZeroDivisionError:
        numberList.clear()
        print("Error: Division by zero.")


while True:
    enterNum = input('Enter number (press enter for operation, or "q" to quit): ')
    if enterNum == "q":
        break
    elif enterNum == "":
        advancedCalc()
    else:
        numberList.append(enterNum)
