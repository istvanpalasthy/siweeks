while True:
    try:
        number_1 = int(input('Enter your first number(or a letter to exit): '))
    except ValueError:
        break
    else:

        operation = str(input('Enter your operation: '))
        number_2 = int(input('Enter your second number: '))

        if operation == "-" :
            print("Result:" ,number_1-number_2)
        elif operation == "+":
            print("Result:" ,number_1+number_2)
        elif operation == "*":
            print("Result:" ,number_1*number_2)
        elif operation == "/":
            print("Result:" ,number_1/number_2)
        else:
            operation == int
            print("Please enter a valid operation!")


    